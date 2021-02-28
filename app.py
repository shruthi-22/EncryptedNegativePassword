from flask import Flask, request, render_template

from internal.aes import aes, aes_decrypt
from internal.helpers import hash_plain_text, perfect_hex, write_to_a_file, is_file_exists, get_hashed_text_binary, \
    read_from_file
from internal.negative_encryption import negative_password, enp_verify

app = Flask(__name__)


@app.route('/register')
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    if is_file_exists('./static/' + str(username)):
        return render_template("message.html", name="Already a user")
    else:
        negative = negative_password(get_hashed_text_binary(password))
        encrypted_negative_passwd = aes(negative, password)
        write_to_a_file('./static/' + str(username), encrypted_negative_passwd)
        return render_template("message.html", name="Successfully Registered")


@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if is_file_exists('./static/' + str(username)):
        try:
            encrypted_negative_password = read_from_file('./static/' + str(username))
            decrypted_negative_password = aes_decrypt(encrypted_negative_password, password)
            if enp_verify(get_hashed_text_binary(password), decrypted_negative_password):
                return render_template("message.html", name="Authorised User")
            else:
                return render_template("message.html", name="Unauthorised User")
        except:
            return render_template("message.html", name="Unauthorised User")
    else:
        return render_template("message.html", name="Please Register")


if __name__ == '__main__':
    app.run()

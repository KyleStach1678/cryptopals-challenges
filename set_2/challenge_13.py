#!/usr/bin/python
import sys
from parse_cookie import parse_cookie
from Crypto import Random
from Crypto.Cipher import AES
from padding import pad

aes = AES.new(Random.get_random_bytes(16), AES.MODE_ECB)

def profile_for(email):
    return 'email={}&uid=10&role=user'.format(email.replace('&', '').replace('=', ''))

def encrypted_profile_for(email):
    return aes.encrypt(pad(profile_for(email), 16))

def decrypted_profile_for(enc):
    return aes.decrypt(enc)

def main(args):
    """
    Do a cut-and-paste attack. Effectively what this will do is align and pad the input so that the
    email is on a block all on its own, specifying "admin" as an email. Then, it will take the ecb
    output block and put that where the role block should go in the encrypted version. When this is
    decrypted, "admin" (padded to an entire block) will show up as the role.
    """
    len_before_email = len('email=')

    attack_email = (16 - len_before_email) * '\0' + pad('admin', 16, '\0')
    len_before_role = len_before_email + len(attack_email) + len('&uid=10&role=')

    extra_pad_length = 16 - len_before_role % 16
    attack_email += '\0' * extra_pad_length

    attack_enc = list(encrypted_profile_for(attack_email))
    admin_block = attack_enc[16:32]

    email = 'kylestach99@gmail.com'
    len_before_role = len_before_email + len(email) + len('&uid=10&role=')
    extra_pad_length = 16 - len_before_role % 16
    actual_enc = list(encrypted_profile_for(email + '\0' * extra_pad_length))
    actual_enc[len_before_role+extra_pad_length:len_before_role+extra_pad_length+16] = admin_block

    print(
        parse_cookie(
            decrypted_profile_for(
                ''.join(actual_enc)
            )
        )
    )

if __name__ == '__main__':
    main(sys.argv[1:])

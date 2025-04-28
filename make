
private_key = account.key.hex()
print(f'Private Key : {private_key}')

public_key =account._key_obj.public_key.to_hex()
print(f"public key: {public_key}")

address =account.address
print(f"address : {address}")
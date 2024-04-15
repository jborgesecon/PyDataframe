from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import x
from bitcoin.core.script import CScript
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

# Define the private key (in WIF format)
private_key_wif = 'your_private_key_here'

# Create a CBitcoinSecret object from the private key
private_key = CBitcoinSecret(private_key_wif)

# Derive the public key (and Bitcoin address) from the private key
public_key = private_key.pub
address = P2PKHBitcoinAddress.from_pubkey(public_key)

print("Your Bitcoin address:", address)

# Define the recipient's address
recipient_address = 'recipient_address_here'

# Define the amount to send (in satoshis)
amount_to_send = 10000

# Create a script that sends funds to the recipient
txout_script = CScript([x('OP_DUP'), x('OP_HASH160'), recipient_address, x('OP_EQUALVERIFY'), x('OP_CHECKSIG')])

# Construct the transaction
tx = CTransaction()
tx.vout.append(CTxOut(amount_to_send, txout_script))

# Sign the transaction with the private key
sighash = SignatureHash(txout_script, tx, 0, SIGHASH_ALL)
sig = private_key.sign(sighash) + bytes([SIGHASH_ALL])
txin_script = CScript([sig, public_key])
tx.vin[0].scriptSig = txin_script

# Verify the transaction
VerifyScript(tx.vin[0].scriptSig, txout_script, tx, 0, (SCRIPT_VERIFY_P2SH,))

print("Transaction successfully signed and verified:")
print(tx)


from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core.script import CScript

# Replace the following with your actual Bitcoin node credentials
rpc_user = 'your_rpc_username'
rpc_password = 'your_rpc_password'
rpc_host = '127.0.0.1'
rpc_port = 8332  # Default Bitcoin RPC port

# Connect to the Bitcoin node's RPC interface
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")

# Replace 'your_address_here' with your Bitcoin address
your_address = 'your_address_here'

try:
    # Get the balance for the specified address
    balance = rpc_connection.getreceivedbyaddress(your_address)

    print("Current balance:", balance)

    # Get transaction history for the specified address
    transactions = rpc_connection.listtransactions("*", 1000)  # Maximum 1000 transactions
    print("Transaction history:")
    for tx in transactions:
        print(tx)

except JSONRPCException as e:
    print("Error:", e)

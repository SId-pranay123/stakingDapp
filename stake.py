import subprocess
import bittensor

def undelegate(wallet_name):
    command = ['btcli', 'root', 'undelegate', '--subtensor.network', "test", '--wallet.name', wallet_name,'--all' ,'--delegate_ss58key', "5Hddm3iBFD2GLT5ik7LZnT3XJUnRnN8PoeCFgGQgawUVKNm8", "--no_prompt"]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Handle errors, print error output
        print(f"Error: {e}")
        print(e.stderr)

def check_balance(wallet_path, wallet_name, network):
    command = ['btcli', 'w', 'balance', '--subtensor.network', network, '--wallet.name', wallet_name, '--wallet.path', wallet_path]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Handle errors, print error output
        print(f"Error: {e}")
        print(e.stderr)

# check_balance("~/.bittensor/wallets/", "gola", "test")

def delegate_tokens(network, wallet_name):
    command = ['btcli', 'root', 'delegate', '--subtensor.network', network, '--wallet.name', wallet_name, '--amount', '1', '--delegate_ss58key', '5Hddm3iBFD2GLT5ik7LZnT3XJUnRnN8PoeCFgGQgawUVKNm8', '--no_prompt']
    print(command)
    try:
        result = subprocess.run(command,capture_output=True, text=True, check=True)
        print("hi")
        print(result)
    except subprocess.CalledProcessError as e:
        # Handle errors, print error output
        print(f"Error: {e}")
        print(e.stderr)


# delegate_tokens("test", "gola")
# undelegate("gola")

def app():
    again = True
    while(again):
        print('1. Check the balance.\n2. Delegate TAO\n3. Undelegate token\n4. For exiting')
        option = input("Enter options(1-4): ")
        if option == '1':
            check_balance("~/.bittensor/wallets/", "gola", "test")
        elif option == '2':
            delegate_tokens("test", "gola")
        elif option == '3':
            undelegate("gola")
        elif option == '4':
            again=False
        else:
            print("Invalid option...Exiting...")

app()
if __name__ == "__main__":
    import sys, os
    from pyngrok import ngrok
    os.system("apt-get install wget")
    os.system("pip install pyspark")
    os.system("apt install openjdk-8-jdk-headless")
    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip ")
    os.system("unzip ngrok-stable-linux-amd64.zip")
    os.system("pip install pyngrok")
    os.system("ngrok update")
    os.system("pip install fastparquet")
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
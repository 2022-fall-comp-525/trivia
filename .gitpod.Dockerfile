FROM ubuntu:latest

# Install custom tools, runtime, etc.
RUN apt update
RUN apt install -y sudo git python3 python3-pip python-is-python3

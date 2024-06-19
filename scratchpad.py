file_name = 'afksjdarlkj3p4orijejfpsdoi uwepiorjasdfdasfsdafiojfdkaejfgggpawoeiafuwepoi fupofiuspfogggiaufdjfggfd hlkgsdjflsdjfkdjfsdkljfpeiotuqpeoriuwproeiwurpoqwiruepqowireuqpweoirupoieurpqoifldksjfhalskjfhlaksjdhlfkajshdflkjashf.txt'
user_name = "robert"
street = 'street'
phone = '342'
FILE_WRITTEN = "success!"
#file_name = file_name[:150]

print(len(file_name))
# Create the file to write to. If OS Error is raised then print error on screen
try:
    with open(file_name, "w") as file:
        file.write(f"{user_name},{street},{phone}")

except OSError as err:
    print('osError', err)

else:
    # print success message when file is written.
    print(f"{FILE_WRITTEN} \"{file_name}\".")
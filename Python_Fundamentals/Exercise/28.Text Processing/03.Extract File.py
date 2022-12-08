""""
Input1                                              Output1
C:\Internal\training-internal\Template.pptx         File name: Template
                                                    File extension: pptx

Input2
C:\Projects\Data-Structures\LinkedList.cs
                                                        Output2
                                                        File name: LinkedList
                                                        File extension: cs
"""

def extract_file(data):

    needed_information = data[-1].split('.')
    file_name = needed_information[0]
    extension = needed_information[1]

    print(f"File name: {file_name}")
    print(f"File extension: {extension}")


d = input().split('\\')
extract_file(d)
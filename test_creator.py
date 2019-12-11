import os

py_file = os.listdir('File to test')[0]
output_filename = 'my_output.txt'
test_inputs = [f'Inputs\\{file}' for file in os.listdir('Inputs')]
test_outputs = [f'Outputs\\{file}' for file in os.listdir('Outputs')]
file_to_test = f'File to test\\{py_file}'


def run_test_command(my_file, test_input, my_output):
    return (f'"{my_file}" < "{test_input}" > {my_output}')


def source_gear_command(file1, file2):
    return (f'sgdm {file1} {file2}')


def build_test_script(script_num, my_file, test_input, test_output, my_output):
    script = open(f'test_{script_num}.bat','w')
    script.write(run_test_command(my_file,test_input,my_output)+'\n')
    script.write(source_gear_command(test_output,my_output))
    script.close()

# build_test_script(1,file_to_test,test_inputs[1],test_outputs[1],output_filename)
tests = zip(test_inputs, test_outputs)

for n, pair in enumerate(tests):
    build_test_script(n+1,file_to_test,pair[0],pair[1],output_filename)

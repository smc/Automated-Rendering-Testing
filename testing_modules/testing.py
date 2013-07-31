import sys
from array import *
  
def renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer, error_file, test_file):
  result_file = open(error_file, 'w')
  reference_file = ref_file_pointer.read()
  rendered_file = rend_file_pointer.read()
  ref_list = []
  rend_list = []
  #Parsing the reference file
  ref_lines = reference_file.replace('[','').replace(']','')
  clean_file = ref_lines.split('\n')
  for aline in clean_file:
    aword = aline.split(',')
    ref_list.append(aword)
  #Parsing the harfbuzz renderings' file
  rend_lines = rendered_file.replace('[','').replace(']','')
  rend_file_lines = rend_lines.split('\n')
  for line in rend_file_lines:
    each_name = line.split('|')
    rend_list.append(each_name)
  rendered_output = []
  for x in rend_list:
    n = []
    for y in x:
      n.append(y.split('=')[0])
    rendered_output.append(n)
  #Opening the file with test cases
  wordfile_content = word_file_pointer.read()
  wordlist = []
  wordlist = wordfile_content.split('\n')
  #Matching rendered glyph names with the reference glyph names
  result_list = []
  result_list = [i for i, j in zip(ref_list, rendered_output) if i != j]
  if result_list == []:
    print "\nNo rendering problems found!"
    sys.exit()
  else:
    print "\nRendering problems observed!\nSee the file " + test_file + " for rendering status of each word and " + error_file + " for the list of wrongly rendered words only.\n"
    a = array('i', [])
  #Finding the wrongly rendered words from the test cases file and writing it to result.txt
    for word in result_list:
      d = ref_list.index(word)
      result_file.write("%d " % (d+1)  + wordlist[d] + '\n')
      a.append(d)
  result_file.close()
  return a, wordlist


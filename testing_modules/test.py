import sys
from array import *
def renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer, result_file):
  reference_file = ref_file_pointer.read()
  rendered_file = rend_file_pointer.read()
  ref_list = []
  rend_list = []
  #Parsing the reference file
  ref_lines = reference_file.replace('[','').replace(']','')
  clean_file = ref_lines.split('\n')
  optional_array = array('i', [])
  optional_list = []
  for aline in clean_file:
    if aline.find(';') != -1:
      optional_array.append(clean_file.index(aline))
      opt_list = aline.split(';')
      for a_glyph in opt_list:
        oneword = a_glyph.split(',')
        optional_list.append(oneword)
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
    f = 1
    a = array('i', [])
  #Finding the wrongly rendered words from the test cases file and writing it to result.txt
    for word in result_list:
      d = ref_list.index(word)
      a.append(d)
  common_words_index = list(set(a).intersection(set(optional_array)))
  for each_term, value in zip(optional_list, common_words_index):
    correct_renderings = list(set(rendered_output[value]).intersection(set(each_term)))
    if correct_renderings != []:
      result_list.pop(value)
      a.remove(value)
  for position in a:
    result_file.write("%d " % (position+1)  + wordlist[position] + '\n')
  return a, wordlist, f
		
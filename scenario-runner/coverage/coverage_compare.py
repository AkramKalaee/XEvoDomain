#This code helps to compare python code coverage reports generated from command
#'coverage report'

'''
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
my/project/example.py                     3      3     0%
'''

import re

def get_coverage( coverage_filename ):
    with open(coverage_filename, mode='r') as infile:
        lines = infile.read().splitlines()
        last_line = lines[-1]
        total_coverage = re.compile('[\d]+%').search(last_line)[0]

    out_map = convert_coverage_report_to_dict_coverage_percent(coverage_filename)
    controller_coverage = "0%"
    for fname, coverage in out_map.items(): #Comaprision, for O(1) for each comparsion O(n)
        if "controller.py" in fname:
            controller_coverage = coverage[0]
            break

    return total_coverage, controller_coverage

def convert_coverage_report_to_dict_coverage_percent( coverage_filename ):
    out_map = {} #{filename: [coverage, missing]}
    with open(coverage_filename, mode='r') as infile:
        #print("Filename: ", coverage_filename)
        for line in infile.readlines():
            if '.py' in line: #only py files
                line = re.sub(' +', ' ',line ) #only spaces are handled here. reports have only spaces
                tmp_list = line.split('%')
                coverage_info = tmp_list[0].split()
                missing_info = tmp_list[1]
                filename = coverage_info[0]
                index = len(coverage_info)
                coverage = coverage_info[index - 1]
                out_map[filename]  = [coverage, [missing_info]]
    return out_map

def convert_coverage_report_to_dict( coverage_filename ):
    out_map = {} #{filename: [coverage, missing]}
    with open(coverage_filename, mode='r') as infile:
        #print("Filename: ", coverage_filename)
        for line in infile.readlines():
            if '.py' in line: #only py files
                line = re.sub(' +', ' ',line ) #only spaces are handled here. reports have only spaces
                tmp_list = line.split('%')
                coverage_info = tmp_list[0].split()
                missing_info = tmp_list[1]
                filename = coverage_info[0]
                coverage = coverage_info[3]
                out_map[filename]  = [coverage, [missing_info]]
    return out_map
    #print(out_map)
            
def compare_coverage_maps(previous_map, latest_map):
    for fname, coverage in previous_map.items(): #Comaprision, for O(1) for each comparsion O(n)
        if fname in latest_map:
            if int(latest_map[fname][0]) != int(previous_map[fname][0]) or latest_map[fname][1] != previous_map[fname][1]:
                print("File: ", fname)
                print("Previous: ",previous_map[fname])
                print("Latest: ",latest_map[fname])
                return False
        else:
            return False

    print("Code coverage change satisfactory")
    return True

def compare():
    prev_coverage = convert_coverage_report_to_dict( PREV_COVERAGE_REPORT_FILE )
    latest_coverage = convert_coverage_report_to_dict( LATEST_COVERAGE_REPORT_FILE)
    return compare_coverage_maps(prev_coverage, latest_coverage)


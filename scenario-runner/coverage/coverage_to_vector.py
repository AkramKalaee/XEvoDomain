import re


def convert_coverage_report_to_dict(coverage_filename):
    out_map = {}  # {filename: [coverage, missing]}
    with open(coverage_filename, mode='r') as infile:
        # print("Filename: ", coverage_filename)
        for line in infile.readlines():
            if '.py' in line:  # only py files
                line = re.sub(' +', ' ', line)  # only spaces are handled here. reports have only spaces
                tmp_list = line.split('%')
                coverage_info = tmp_list[0].split()
                missing_info = tmp_list[1]
                filename = coverage_info[0]
                coverage = coverage_info[3]
                out_map[filename] = [coverage, [missing_info]]
    return out_map
    # print(out_map)

def convert_coverage_report_to_vector(target_report, current_report):
    target_coverage = convert_coverage_report_to_dict(target_report)

    path_1 = []
    path_2 = []
    branch_points = []

    for fname in target_coverage.keys():
        missing_1 = target_coverage[fname][1][0]
        branches_1 = [x for x in re.compile("[\d]+->[\d]+|[\d]+->exit").findall(missing_1) if x is not '']
        statements_1 = list(set(re.sub(r"\s+", "", missing_1).split(',')) - set(branches_1))

        current_coverage = convert_coverage_report_to_dict(current_report)
        if fname in current_coverage:
            missing_2 = current_coverage[fname][1][0]
            branches_2 = [x for x in re.compile("[\d]+->[\d]+|[\d]+->exit").findall(missing_2) if x is not '']
            statements_2 = list(set(re.sub(r"\s+", "", missing_2).split(',')) - set(branches_2))
        else:
            branches_2 = ""

        branch_no = len(branches_1)
        jump = False
        for idx in range(branch_no):
            if jump:
                jump = False
                continue
            branch_1 = branches_1[idx]
            _from_to_1 = branch_1.split('->')
            _from_1 = int(_from_to_1[0])

            try:
                _to_1 = int(_from_to_1[1])
            except:
                _to_1 = _from_to_1[1]

            if idx != branch_no - 1:
                nex_branch = branches_1[idx + 1]
                if int(nex_branch.split('->')[0]) == _from_1:
                    jump = True
                    continue

            branch_list = re.compile("{}->[\d]+|{}->exit".format(_from_1, _from_1)).findall("".join(branches_2))
            branch_2 = [x for x in branch_list if x is not '']

            if not branch_2:
                if isinstance(_to_1, int) and _to_1 == _from_1 + 1:  # true branch
                    true_branch = branch_1
                    false_branch = "{}->exit".format(_from_1)
                    branch_1_TValue = 0
                    branch_1_FValue = 1
                    branch_2_TValue = 0
                    branch_2_FValue = 0
                else:
                    true_branch = "{}->{}".format(_from_1, _from_1 + 1)
                    false_branch = branch_1
                    branch_1_TValue = 1
                    branch_1_FValue = 0
                    branch_2_TValue = 0
                    branch_2_FValue = 0

                branch_points.append(true_branch)
                branch_points.append(false_branch)

                path_1.append(branch_1_TValue)
                path_1.append(branch_1_FValue)

                path_2.append(branch_2_TValue)
                path_2.append(branch_2_FValue)
                continue

            branch_2 = branch_2[0]
            _from_to_2 = branch_2.split('->')
            try:
                _to_2 = int(_from_to_2[1])
            except:
                 _to_2 = _from_to_2[1]

            if (isinstance(_to_1, int) and isinstance(_to_1, int)) or (isinstance(_to_1, str) and isinstance(_to_1, str)) and _to_1 == _to_2:
                if isinstance(_to_1, int):
                    if _to_1 == _from_1 + 1: #true branch
                        true_branch = branch_1
                        false_branch = "{}->exit".format(_from_1)
                        branch_1_TValue = 0
                        branch_1_FValue = 1
                        branch_2_TValue = 0
                        branch_2_FValue = 1
                    else:
                        true_branch = "{}->{}".format(_from_1, _from_1 + 1)
                        false_branch = branch_1
                        branch_1_TValue = 1 #covers true branch
                        branch_1_FValue = 0
                        branch_2_TValue = 1
                        branch_2_FValue = 0
                else:
                        true_branch = "{}->{}".format(_from_1, _from_1 + 1)
                        false_branch = branch_1
                        branch_1_TValue = 1 #covers true branch
                        branch_1_FValue = 0
                        branch_2_TValue = 1
                        branch_2_FValue = 0

            else:
                if isinstance(_to_1, int) and isinstance(_to_2, int):
                    if _to_1 < _to_2:
                        true_branch = branch_1
                        false_branch = branch_2
                        branch_1_TValue = 0
                        branch_1_FValue = 1
                        branch_2_TValue = 1
                        branch_2_FValue = 0
                    else:
                        true_branch = branch_2
                        false_branch = branch_1
                        branch_1_TValue = 1
                        branch_1_FValue = 0
                        branch_2_TValue = 0
                        branch_2_FValue = 1
                else:
                    if isinstance(_to_1, int):
                        true_branch = branch_1
                        false_branch = branch_2
                        branch_1_TValue = 0
                        branch_1_FValue = 1
                        branch_2_TValue = 1
                        branch_2_FValue = 0
                    else:
                        true_branch = branch_2
                        false_branch = branch_1
                        branch_1_TValue = 1 #covers true branch
                        branch_1_FValue = 0
                        branch_2_TValue = 0
                        branch_2_FValue = 1

            branch_points.append(true_branch)
            branch_points.append(false_branch)

            path_1.append(branch_1_TValue)
            path_1.append(branch_1_FValue)

            path_2.append(branch_2_TValue)
            path_2.append(branch_2_FValue)

        branch_no = len(branches_2)
        jump = False
        for idx in range(branch_no):
            if jump:
                jump = False
                continue
            branch_2 = branches_2[idx]
            _from_to_2 = branch_2.split('->')
            _from2 = int(_from_to_2[0])

            try:
                _to_2 = int(_from_to_2[1])
            except:
                _to_2 = _from_to_2[1]

            if idx != branch_no - 1:
                nex_branch = branches_2[idx + 1]
                if int(nex_branch.split('->')[0]) == _from2:
                    jump = True
                    continue

            branch_list = re.compile("{}->[\d]+|{}->exit".format(_from2, _from2)).findall("".join(branches_1))
            branch_1 = [x for x in branch_list if x is not '']
            if not branch_1:
                if isinstance(_to_2, int) and _to_2 == _from2 + 1:  # true branch
                    true_branch = branch_2
                    false_branch = "{}->exit".format(_from2)
                    branch_1_TValue = 0
                    branch_1_FValue = 0
                    branch_2_TValue = 0
                    branch_2_FValue = 1
                else:
                    true_branch = "{}->{}".format(_from2, _from2 + 1)
                    false_branch = branch_2
                    branch_1_TValue = 0
                    branch_1_FValue = 0
                    branch_2_TValue = 1
                    branch_2_FValue = 0

                branch_points.append(true_branch)
                branch_points.append(false_branch)

                path_1.append(branch_1_TValue)
                path_1.append(branch_1_FValue)

                path_2.append(branch_2_TValue)
                path_2.append(branch_2_FValue)

    return [path_1, path_2]


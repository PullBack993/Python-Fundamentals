# @#+[A-Za-z0-9]{6,}@#+
import re
barcode_count = int(input())
pattern = r"^@#+([A-Za-z0-9A-Z]{5,}[A-Z])@#+$"
group_barcode = []
counter = ""
check_if_regex = False
for n in range(barcode_count):
    barcode = input()
    check_if_regex = False
    for el in re.findall(pattern, barcode):
        for i in el:
            if i.isdigit():
                counter += i
        if counter:
            group_barcode.append(counter)
            counter = ""
            check_if_regex = True
        else:
            check_if_regex = True
            group_barcode.append('00')
    if not check_if_regex:
        print("Invalid barcode")
    else:
        print(f'Product group: {"".join(group_barcode)}')
        group_barcode = []
# import re
#
#
# pattern = r'(^@#+)(?P<code>[A-Z][A-Za-z0-9]{4,}[A-Z])(@#+$)'
# nums_pattern = r'\d'
#
# n = int(input())
# for _ in range(n):
#     data = input()
#     m = re.fullmatch(pattern, data)
#     if not m:
#         print('Invalid barcode')
#         continue
#     code = m.group('code')
#     nums = re.findall(nums_pattern, code)
#     product_group = '00'
#     if len(nums) != 0:
#         product_group = ''.join(nums)
#     print(f'Product group: {product_group}')
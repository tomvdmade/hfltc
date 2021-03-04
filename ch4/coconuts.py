i = 0

smoothies = ['coconut', 'strawberery', 'banana', 'tropical', 'acai berry']
has_coconut = [ True, False, False, True, False]

# while i < len(has_coconut):
#     if has_coconut[i]:
#         print(smoothies[i], 'contains cononut')
#     i = i + 1   

lenght = len(smoothies)
for i in range(lenght):
    if has_coconut[i]:
        print(smoothies[i], 'contains cononut')
    i = i + 1   

# for smoothie in smoothies:
#     output = 'We serve ' + smoothie
#     print(output)
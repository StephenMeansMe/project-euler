sm_list = [i for i in range(1,10) if i % 3 == 0 or i % 5 == 0]
print(sm_list)
print(sum(sm_list))

big_list = [num for num in range(1,1000) if num % 3 == 0 or num % 5 == 0] 
results = sum(big_list)
str_results = str(results)
with open('results','w') as results_file:
    results_file.write(str_results)

print("The sum is:",results)

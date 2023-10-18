#!/usr/bin/env python3

original_seq = 'ATGCAGGGGAAACATGATTCAGGAC'
print(original_seq)
reverse_original_seq = print(original_seq[::-1]) # returns 'CAGGACTTAGTACAAAGGGGACGTA'
reverse_original_seq = 'CAGGACTTAGTACAAAGGGGACGTA'
print(reverse_original_seq)
reverse_original_seq_lower = reverse_original_seq.lower()
print(reverse_original_seq_lower)

replace_a_T = reverse_original_seq_lower.replace('a','T')
print(replace_a_T)
replace_t_A = replace_a_T.replace('t','A')
print(replace_t_A)
replace_g_C = replace_t_A.replace('g','C')
print(replace_g_C)
replace_c_G = replace_g_C.replace('c','G')
print(replace_c_G)









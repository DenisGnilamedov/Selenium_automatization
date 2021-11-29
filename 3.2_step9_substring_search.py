s = '1'

if '1' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


test_substring(input(), input())


# vietnamese-syllable-regex
Split Vietnamese syllable into onset and rime

Các kí tự nguyên âm có dấu:
```
aàáảãạ
oòóỏõọ
ôồốổỗộ
ơờớởỡợ
uùúủũụ
ưừứửữự

ăằắẳẵặ
âầấẩẫậ

eèéẻẽẹ
êềếểễệ
iìíỉĩị
yỳýỷỹỵ
```

## phụ âm

### phụ âm đặc biệt

#### nhóm `qu_`, `gi_`
- tính vần u_/i_
```python
'quôc'  # -> uôc, chỉ có 1 TH là 'quốc'

'giê([mu]|[cpt]|ng?)'  # -> iê_
'gin?|gi(p|ich)'       # -> i*
```
- tính vần đằng sau qu/gi
```python
'quy.*'   # -> i*
'qu(.+)'  # rồi kiểm tra vần hợp lệ
'gi(.+)'
```

#### không có phụ âm đầu, chỉ có vần
-> trường hợp `iê_` biến thành `yê_`
```python
'(i[^ê]|[^i]).+'  # rồi kiểm tra vần hợp lệ
## nhóm `y_`
'yê([mu]|ng?)'
'yêt'
```

### phụ âm thường

#### nhóm đi với mọi vần
```python
'[bdđlmnprsvx]|[cknp]?h|t[hr]?'
```
#### nhóm eiy ('eêiy'):
```python
'k|n?gh'
```
#### nhóm aou ('aăâoôơuư'):
```python
'c|n?g'
```
## vần

### vần đơn
```python
'[aàáảãạeèéẻẽẹêềếểễệiìíỉĩịoòóỏõọôồốổỗộơờớởỡợuùúủũụưừứửữựyỳýỷỹỵ]'
```
### "oa", "oe", "uê", "uy" có 2 cách bỏ dấu
#### bỏ dấu kiểu cũ
```python
'[oòóỏõọ][ae]'
'[uùúủũụ][êy]'
```
#### bỏ dấu kiểu mới
```python
'o[aàáảãạeèéẻẽẹ]'
'u[êềếểễệyỳýỷỹỵ]'
```
### bình thường

gồm 2 nhóm:
- sắc/nặng
- mọi dấu

#### rút gọn
##### `[cpt]|ch`: sắc/nặng
```python
'([ăâeou]|iê|o?a|u?ô|ươ)[cpt]'
'[êiơ][pt]'
'(ư|oă)[ct]'
'ooc'
'(oe|uâ|uyê?)t'
'([êi]|o?a|u[êy])ch'
```
##### `[aimouy]|n[gh]?`: mọi dấu
```python
'([iuư]|uy)a'
'([ouư]|o?a|u?ô|ư?ơ)i'
'o?[ae]o'
'([aâiư]|uy|ươ|i?ê)u'
'(o?a|u?â)y'
'([âeouư]|o?[aă]|iê|u?ô|ươ)(m|ng?)'  # có m, n, g
'([êiơ]|oe)[mn]'  # chỉ m, n
'uâng?'  # chỉ n, ng
'uyê?n'  # chỉ n
'oong'  # chỉ ng
'([êi]|o?a|u[êy])nh'
```
#### đầy đủ
```python
'a([imouy]|n[gh]?)'
'a([cpt]|ch)'

'ă(m|ng?)'
'ă[cpt]'

'â([muy]|ng?)'
'â[cpt]'

'e([mo]|ng?)'
'e[cpt]'

'ê([mu]|nh?)'
'ê([pt]|ch)'

'i([amu]|nh?)'
'i([pt]|ch)'
'iê([mu]|ng?)'
'iê[cpt]'

'o([im]|ng?)'
'o[cpt]'
'oa([imoy]|n[gh]?)'
'oa([cpt]|ch)'
'oă(m|ng?)'
'oă[cpt]'
'oe[mno]'
'oet'
'oong'
'ooc'

'ô([im]|ng?)'
'ô[cpt]'

'ơ[imn]'
'ơ[pt]'

'u([aim]|ng?)'
'u[cpt]'
'uâ(y|ng?)'
'uât'
'uênh'
'uêch'
'uô([im]|ng?)'
'uô[cpt]'
'uơ'
'uy([au]|nh?)'
'uy([pt]|ch)'
'uyên'
'uyêt'

'ư([aimu]|ng?)'
'ư[ct]'  # ư[cpt]
'ươ([imu]|ng?)'
'ươ[cpt]'

'yê([mu]|ng?)'
'yêt'
```

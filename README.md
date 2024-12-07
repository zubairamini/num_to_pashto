# Number Digit to Pashto Words Python

`num_to_pashto` is a python function that converts numbers into their equivalent Pashto words. It supports a wide range of numbers, including positive and large values up to billions. The function is ideal for educational tools, financial applications, and Pashto-language user interfaces or A Python library for seamless conversion between Pashto and English numeric formats. It provides utilities for converting numbers, handling numeric translations, and ensuring accurate Pashto digit representation. 

## Features

- Converts numbers to Pashto words, from **0** to billions.
- Handles **positive** , **negative** and **fractions**  numbers.
- Supports **thousands**, **lakhs (لکه)**, **millions (میلیون)**, and **billions (میلیارد)**.
- Special handling for numbers ending in **20**, displaying "شل" or "ویشت" appropriately.
- Numbers represented in Pashto digits (۰, ۱, ۲, ۳, ۴, ۵, ۶, ۷, ۸, ۹) are accurately handled during conversion to words.

---

## Examples

### Basic Conversions

| Number | Pashto Word (Output)               |
|--------|------------------------------------|
| 10      | لس                             |
| 25     | پنځه ویشت                                |
| ۲۰    | شل                          |
| 100    | سل                                |
| 924382 | نه لکه څلور ویشت زره دری سوه دوه اتیا |
| 5.34    | پنځه اعشاریه دری څلور                  |
| ۵.۳۴    | پنځه اعشاریه دری څلور                  |
| ۸    | اته                  |

---

### Handling Special Cases

1. **Standalone 20**:  
   - Input: `20`  
   - Output: **شل**  

2. **Numbers ending in 20**:  
   - Input: `324`  
   - Output: **دری سوه څلور ویشت**

3. **Special handling for 20000**:  
   - Input: `20000`  
   - Output: **شل زره**
  
4. **Special handling for ۸**:  
   - Input: `20000`  
   - Output: **اته**

---



### Large Numbers

| Number     | Pashto Word (Output)                                 |
|------------|------------------------------------------------------|
| 345678     |دری لکه پينځه څلویښت زره شپږ سوه او اته اویا                 |
| ۱۰۰۰۰۰۰    | یو میلیون                                           |
| 1000000000 | یو میلیارد                                           |

---

## Limitations
- Complex number formatting for currency or financial outputs is not supported.


## Recommendation
- Further research is needed to improve and refine Pashto literature related to numbers

- 
## Usage

1. Pass the input number to the function like num_to_pashto(20) or num_to_pashto('۲۰').
2. The function returns the Pashto equivalent as a string.
3. Use the output directly for display in user interfaces or reports.
   
example

let result = digitToPashtoWord(12045);

console.log(result); // Outputs: "دولس زره پنځه څلویښت"

---
# num_to_pashto
A Python library for seamless conversion between Pashto and English numeric formats. It provides utilities for converting numbers, handling numeric translations, and ensuring accurate Pashto digit representation. Developed by Ahmad Zubair Amini

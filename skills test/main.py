
from pyscript import document

def validateForm(event=None):
    fname = document.getElementById("fname").value.strip()
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value
    result = document.getElementById("result")

   
    name_valid = fname.istitle()

    
    username_valid = len(username) >= 7

    
    p_len = len(password) >= 10
    p_let = any(c.isalpha() for c in password)
    p_num = any(c.isdigit() for c in password)
    password_valid = p_len and p_let and p_num

    # ----- Final Decision -----
    if not name_valid:
        result.innerText = " Full Name must be in Title Case"
    elif not username_valid:
        result.innerText = "Username must be at least 7 characters long"
    elif not password_valid:
        result.innerText = (
            "Password must be at least 10 characters long and contain "
            "at least one letter and one number"
        )
    else:
        result.innerText = "✅ Account successfully created!"




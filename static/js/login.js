document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
      
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
  
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
  
    let isValid = true;
  
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!email) {
          document.getElementById('email-error').textContent = 'Email обязателен';
          isValid = false;
      } else if (!emailRegex.test(email)) {
          document.getElementById('email-error').textContent = 'Неверный формат email';
          isValid = false;
      }
  
  
      if (password.length < 1) {
      document.getElementById('password-error').textContent = 'Введите пароль';
      isValid = false;
    }
  
    if (isValid) {
       // эмуляция успешного входа
        document.getElementById('success-message').style.display = 'block';
        document.getElementById('error-message').style.display = 'none';
  
        //сбросить форму и убрать сообщение
        setTimeout(function() {
            document.getElementById('login-form').reset();
            document.getElementById('success-message').style.display = 'none';
      }, 3000);
  
  
       // Здесь можно добавить код для отправки данных на сервер и проверки учетных данных
    } else {
          document.getElementById('error-message').style.display = 'block';
          document.getElementById('success-message').style.display = 'none';
      
        }
  });
  
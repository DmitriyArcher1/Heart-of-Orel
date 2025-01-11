document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    // Сброс предыдущих ошибок
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
  
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
  
    let isValid = true;
  
    if (!username) {
        document.getElementById('username-error').textContent = 'Имя пользователя обязательно';
        isValid = false;
    }
  
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!email) {
          document.getElementById('email-error').textContent = 'Email обязателен';
          isValid = false;
      } else if (!emailRegex.test(email)) {
          document.getElementById('email-error').textContent = 'Неверный формат email';
          isValid = false;
      }
  
      if (password.length < 8) {
      document.getElementById('password-error').textContent = 'Пароль должен содержать не менее 8 символов';
      isValid = false;
    }
  
    if (password !== confirmPassword) {
      document.getElementById('confirm-password-error').textContent = 'Пароли не совпадают';
      isValid = false;
    }
  
    if (isValid) {
      document.getElementById('success-message').style.display = 'block';
      // здесь можно добавить код для отправки данных на сервер
  
      setTimeout(function() {
        document.getElementById('registration-form').reset();
        document.getElementById('success-message').style.display = 'none';
  
      }, 3000); // сообщение исчезнет через 3 секунды
    }
  });
  
const saveButton = document.querySelector('.save-btn');
const card = saveButton.closest('.card');

saveButton.addEventListener('click', () => {
  card.classList.toggle('saved');
});

// لتفعيل أو تعطيل حساب المعلم
document.getElementById('activateSwitch').addEventListener('change', function() {
    if (this.checked) {
        alert('Teacher account activated!');
    } else {
        alert('Teacher account deactivated.');
    }
});

// شيفرة للتفاعل مع عناصر معينة إذا لزم الأمر
$(document).ready(function() {
    console.log("Ready!");
    // يمكن إضافة أحداث إضافية هنا إذا احتاج المشروع
});

// البحث عن معلم في البطاقات
document.querySelector('.input-group button').addEventListener('click', function() {
    const searchQuery = document.querySelector('.input-group input').value.toLowerCase();
    const cards = document.querySelectorAll('.teacher-card');

    cards.forEach(card => {
        const teacherName = card.querySelector('.card-title').innerText.toLowerCase();
        if (teacherName.includes(searchQuery)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
});

// تفعيل الـ tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});


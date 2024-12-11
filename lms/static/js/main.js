// ============================================================

const saveButton = document.querySelector('.save-btn');
const card = saveButton.closest('.card');

saveButton.addEventListener('click', () => {
  card.classList.toggle('saved');
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

//===============================================================

const targetDate = new Date(new Date().getTime() + 2 * 24 * 60 * 60 * 1000).getTime();

const countdownInterval = setInterval(function () {
    const now = new Date().getTime();
    const timeLeft = targetDate - now;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    document.getElementById("days").textContent = days;
    document.getElementById("hours").textContent = hours;
    document.getElementById("minutes").textContent = minutes;
    document.getElementById("seconds").textContent = seconds;

    if (timeLeft <= 0) {
        clearInterval(countdownInterval);
        document.querySelector('.countdown').style.display = 'none';
        document.getElementById('offer-ended').style.display = 'block';
    }
}, 1000);
// amr haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
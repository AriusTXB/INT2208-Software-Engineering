document.addEventListener("DOMContentLoaded", function () {
    /*Dropdown menu*/
    const moreButton = document.getElementById("more-button");
    const dropdownMenu = moreButton.nextElementSibling;

    dropdownMenu.style.display = "none";
    moreButton.addEventListener("mouseover", function (event) {
        event.preventDefault(); // Ngăn chặn link tự động chuyển trang
        dropdownMenu.style.display = (dropdownMenu.style.display === "block") ? "none" : "block";
    });

    document.addEventListener("mouseout", function (event) {
        if(!dropdownMenu.contains(event.relatedTarget)) {
            dropdownMenu.style.display = "none";
        }
    });

    dropdownMenu.addEventListener("mouseover", function () {
        dropdownMenu.style.display = "block";  // Giữ menu hiển thị khi di chuột vào menu
    });

    dropdownMenu.addEventListener("mouseout", function (event) {
        if (!moreButton.contains(event.relatedTarget)) {
            dropdownMenu.style.display = "none";  // Ẩn menu khi chuột ra khỏi menu
        }
    });

    /*Search action*/
    const searchButton = document.getElementById("searchBtn");
    const closeSearchButton = document.getElementById("closeSearchBtn");
    const searchOverlay = document.getElementById("searchOverlay");
    if(searchButton && searchOverlay) {
        searchButton.addEventListener('click', function() {
            searchOverlay.classList.add('active');
            searchOverlay.querySelector('input').focus();
        });
    }

    if(closeSearchButton && searchOverlay) {
        closeSearchButton.addEventListener('click', function() {
            searchOverlay.classList.remove('active');
        });
    }

    // Login - Register
    const authTabs = document.querySelectorAll('.auth-tab');

    if (authTabs.length > 0) {
        authTabs.forEach(tab => {
            tab.addEventListener('click', function() {
                // Remove active class from all tabs
                document.querySelectorAll('.auth-tab').forEach(t => {
                t.classList.remove('active');
                });

                // Hide all tab contents
                document.querySelectorAll('.auth-form').forEach(form => {
                form.classList.remove('active');
                });

                // Add active class to clicked tab
                this.classList.add('active');

                // Show corresponding form
                const tabId = this.getAttribute('data-tab');
                document.getElementById(tabId + 'Form').classList.add('active');
            });
        });
    }

    // login facebook
    document.querySelector('.facebook-btn').addEventListener('click', function(){
        window.location.href = 'https://www.facebook.com/login.php'
    });
    // login google
    document.querySelector('.google-btn').addEventListener('click', function(){
        window.location.href = 'https://accounts.google.com/signin'
    });

    // login control
    const loginForm = document.querySelector('#loginForm form');
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const email = document.getElementById('login-email').value.trim();
            const password = document.getElementById('login-password').value;

            fetch('../../Database/users.json') // đường dẫn tới users.json
                .then(response => response.json())
                .then(users => {
                    const user = users.find(u => u.email === email && u.password === password);
                    if (user) {
                        sessionStorage.setItem('loggedInUser', JSON.stringify(user));
                        alert("Đăng nhập thành công!");
                        window.location.href = "HomepageGuest.html"; // sau login chuyển về Homepage
                    } else {
                        alert("Email hoặc mật khẩu không đúng!");
                    }
                })
                .catch(err => {
                    console.error("Lỗi khi đọc file users.json", err);
                    alert("Không thể đăng nhập lúc này.");
                });
        });
    }
});

// reaction
document.querySelector('.love-button').addEventListener('click', function() {
    this.classList.toggle('active');
});

// summarize
document.addEventListener("DOMContentLoaded", function () {
    const summarizeButton = document.querySelector(".summarize-button");
    const fullContent = document.querySelector(".main-content:not(.active)");
    const summarizedContent = document.querySelector(".main-content.active");
    const loadingSpinner = document.querySelector(".loading-spinner");

    // Ban đầu: hiển thị nội dung gốc, ẩn nội dung tóm tắt
    summarizedContent.style.display = "none";

    summarizeButton.addEventListener("click", function () {
        if (fullContent.style.display !== "none") {
            // Chuyển sang tóm tắt
            summarizeButton.disabled = true;
            loadingSpinner.style.display = "block";
            setTimeout(() => {
                fullContent.style.display = "none";
                summarizedContent.style.display = "block";
                summarizeButton.textContent = "Read original article";
                loadingSpinner.style.display = "none";
                summarizeButton.disabled = false;
            }, 10000); // 10 giây giả lập
        } else {
            // Quay lại nội dung gốc
            fullContent.style.display = "block";
            summarizedContent.style.display = "none";
            summarizeButton.textContent = "Summarize this article";
        }
    });
});

function showSpinner() {
    const fullContent = document.querySelector(".main-content:not(.active)");
    const loadingSpinner = document.querySelector(".loading-spinner");

    if (fullContent && fullContent.style.display !== "none") {
        // Hiển thị spinner khi đang tóm tắt bài viết
        document.getElementById("spinner").style.display = "block";
        loadingSpinner.style.display = "block";

        setTimeout(() => {
            // Ẩn spinner sau khi tóm tắt xong
            document.getElementById("spinner").style.display = "none";
            loadingSpinner.style.display = "none";
        }, 10000); // 
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Kiểm tra trạng thái đăng nhập từ sessionStorage
    const checkLogIn = sessionStorage.getItem("loggedInUser");

    // Lắng nghe sự kiện nhấn nút "Summarize this article"
    const summarizeButton = document.querySelector(".summarize-button");
    if (summarizeButton) {
        summarizeButton.addEventListener("click", function(event) {
            // Nếu chưa đăng nhập, chuyển hướng đến trang đăng nhập
            if (!checkLogIn) {
                window.location.href = "Login.html"; // Chuyển đến trang đăng nhập
            } 
        });
    }
});

// search logic

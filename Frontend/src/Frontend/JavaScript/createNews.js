function addTextBlock(content = '') {
    const editor = document.getElementById("editor");
    const block = document.createElement('div');
    block.className = 'block text-block'; // Thêm class text-block để phân biệt

    const textarea = document.createElement('textarea');
    textarea.placeholder = "Write your article...";
    textarea.value = content; // Gán nội dung nếu có

    const removeBtn = document.createElement('button');
    removeBtn.innerHTML = '<i class="fas fa-trash"></i>';
    removeBtn.className = 'remove-btn';
    removeBtn.onclick = () => block.remove();

    block.appendChild(removeBtn);
    block.appendChild(textarea);
    editor.appendChild(block);
}

function addImageBlock(imageSrc = '') {
    const editor = document.getElementById('editor');
    const block = document.createElement('div');
    block.className = 'block image-block'; // Thêm class image-block để phân biệt

    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';

    const preview = document.createElement('img');
    preview.className = 'preview';
    if (imageSrc) {
        preview.src = imageSrc;
        preview.style.display = 'block';
    } else {
        preview.style.display = 'none';
    }

    fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                preview.src = event.target.result;
                preview.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    }

    const removeBtn = document.createElement('button');
    removeBtn.innerHTML = '<i class="fas fa-trash"></i>';
    removeBtn.className = 'remove-btn';
    removeBtn.onclick = () => block.remove();

    block.appendChild(removeBtn);
    block.appendChild(fileInput);
    block.appendChild(preview);
    editor.appendChild(block);
}

// save and submit
function saveDraft() {
    const category = document.getElementById('category').value;
    const editor = document.getElementById('editor').children;

    const blocks = [];

    for (let block of editor) {
        if (block.classList.contains('text-block')) {
            const textarea = block.querySelector('textarea');
            blocks.push({
                type: "text",
                content: textarea.value
            });
        } else if (block.classList.contains('image-block')) {
            const img = block.querySelector('img');
            blocks.push({
                type: "image",
                content: img.src // Lưu src chứ không phải input file
            });
        }
    }

    const draft = {
        category: category,
        blocks: blocks
    };

    localStorage.setItem('draftArticle', JSON.stringify(draft));
    alert('Draft saved!');
}

function loadDraft() {
    const draft = JSON.parse(localStorage.getItem('draftArticle'));
    if (draft) {
        if (draft.category) {
            document.getElementById('category').value = draft.category;
        }
        if (draft.blocks) {
            for (let block of draft.blocks) {
                if (block.type === "text") {
                    addTextBlock(block.content);
                } else if (block.type === "image") {
                    addImageBlock(block.content);
                }
            }
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    loadDraft();

    document.getElementById('saveDraftBtn').addEventListener('click', saveDraft);
});
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.like-btn').forEach(button => {
    button.addEventListener('click', () => {
      const postId = button.getAttribute('data-post-id');

      fetch(`/like/${postId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
        }
      })
      .then(res => res.json())
      .then(data => {
        const countSpan = document.getElementById(`like-count-${postId}`);
        countSpan.textContent = data.likes;
        button.classList.toggle('liked', data.liked);
      });
    });
  });

  function getCookie(name) {
    const cookie = document.cookie
      .split('; ')
      .find(row => row.startsWith(name + '='));
    return cookie ? decodeURIComponent(cookie.split('=')[1]) : null;
  }
});
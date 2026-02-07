document.addEventListener('DOMContentLoaded', () => {
    const courseCards = document.querySelectorAll('.course-card');
    const courseDetailPanel = document.getElementById('course-detail-panel');

    courseCards.forEach(card => {
        card.addEventListener('click', async (event) => {
            const courseId = card.dataset.courseId;
            try {
                const response = await fetch(`/api/course/${courseId}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const course = await response.json();
                displayCourseDetails(course);
            } catch (error) {
                console.error('Error fetching course details:', error);
                courseDetailPanel.innerHTML = '<p>Error loading course details.</p>';
            }
        });
    });

    function displayCourseDetails(course) {
        let topicsHtml = '';
        if (course.topics && course.topics.length > 0) {
            topicsHtml = '<h4>Topics Covered:</h4><ul>';
            course.topics.forEach(topic => {
                topicsHtml += `<li>${topic}</li>`;
            });
            topicsHtml += '</ul>';
        } else {
            topicsHtml = '<p>No topics listed for this course.</p>';
        }

        courseDetailPanel.innerHTML = `
            <h2>${course.title}</h2>
            <p>${course.description}</p>
            <p class="instructor">Instructor: ${course.instructor}</p>
            <p>Duration: ${course.duration}</p>
            ${topicsHtml}
        `;
    }
});

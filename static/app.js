axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


new Vue({
    el: '#images_app',
    data: {
        images: [],
        newImage: {
            description: '',
            image_data: ''
        }
    },
    methods: {
        requestData: function () {
            const vm = this;
            axios.get('/api/images/')
                .then(function (response) {
                    vm.images = response.data;
                })
                .catch(function (error) {
                    console.error('Error fetching data:', error);
                });
        },
        addImageData: function () {
            const vm = this;
            // Отправка данных на сервер для добавления в базу данных
            axios.post('/api/images/', vm.newImage)
                .then(function (response) {
                    // Обновление списка изображений после успешного добавления
                    vm.requestData();
                    // Очистка формы
                    vm.newImage = {
                        description: '',
                        image_data: ''
                    };
                })
                .catch(function (error) {
                    console.error('Error adding data:', error);
                });
        },
        deleteImageData: function (imageId) {
            const vm = this;
            axios.delete(`/api/images/${imageId}/`)
                .then(function (response) {
                    // Обновление списка изображений после успешного удаления
                    vm.requestData();
                })
                .catch(function (error) {
                    console.error('Error deleting data:', error);
                });
        }
    }
});

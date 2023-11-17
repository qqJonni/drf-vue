new Vue({
    el: '#images_app',
    data: {
        images: []
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
        }
    }
});

const app = Vue.createApp({
    data() {
        return {
            display: ''
        }
    },
    methods: {
        add() {
            this.display += '+';
        },
        subtract() {
            this.display += '-';
        },
        divide() {
            this.display += '/';
        },
        multiply() {
            this.display += '*';
        },
        equals() {
            this.display = eval(this.display);
        }
    }
})

app.mount('#app')

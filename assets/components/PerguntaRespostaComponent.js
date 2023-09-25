
export const PerguntaResposta = {
    setup() {
    },
    mounted() {
    },
    data() {

        const notificacao = {
            mostrar: false,
            tipo: 'is-success',
            mensagem: ''
        }

        return {
            notificacao
        }
    },
    methods: {
        fetchCategorias() {
            this.carregandoCategorias = true
            fetch('/api/categorias')
                .then(response => {
                    if (!response.ok)
                        throw Error("Erro buscando categorias")
                    return response.json()
                })
                .then(data => {
                    this.categorias = data
                })
                .catch(error => {
                    console.log(error)
                    this.notificacao.mensagem = error.message
                    this.notificacao.tipo = 'is-danger'
                    this.notificacao.mostrar = true
                })
                .finally(() => {
                    this.carregandoCategorias = false
                });
        },        
    },
    template: `
    <div class="block">
        <div class="columns is-vcentered is-mobile">
            <div class="column">
                <div class="block is-size-5">
                    <p>Indique a variável com o nome <strong>errado</strong>:</p>
                </div>
            </div>
        </div>
    </div>
    `
}
const { createApp } = Vue

import { PerguntaResposta } from './components/PerguntaRespostaComponent.js'

createApp({    
    components: {
        PerguntaResposta
    },
    setup() {
    },
    data() {
        let carregandoRegistros = false

        return {
            carregandoRegistros
        }
    }
})
.mount("#app")    
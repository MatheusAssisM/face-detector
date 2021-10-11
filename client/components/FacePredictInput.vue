<template>
    <div class="input_file">
        <b-form-file
            v-model="file"
            :state="Boolean(file)"
            placeholder="Escoha ou solte uma imagem aqui..."
            drop-placeholder="Solte aqui"
            accept=".jpg, .png"
            :file-name-formatter="formatFileName"
        />
        <button 
            type="button" 
            class="btn btn-primary"
            @click="findFaces()"
            :disabled="!file"
        >
            Enviar
        </button>
    </div>
</template>

<script>
export default {
    data () {
        return {
            file: null,
        }
    },
    methods: {
        formatFileName(file) {
            if (file.length) {
                return file[0].name
            }
            return 'Escolha um arquivo'
        },

        async findFaces () {
            if (!this.file) {
                return
            }
            const faces = await this.$store.dispatch('facePredictor/findFaces', this.file)
            this.callFacePredictViewer(faces)

            if (!faces) {
                this.showAlert(
                    'danger', 
                    {
                        body: 'Alguma coisa deu errada!',
                        title: 'Erro'
                    }
                )
                return
            }
        },

        showAlert (variant, {title, body}) {
            this.$bvToast.toast(body, {
                title,
                autoHideDelay: 5000,
                variant
            })
        },

        callFacePredictViewer (faces) {
            const imagesBase64 = faces?.result?.faces_images
            this.$bus.$emit('show-image', imagesBase64)
        }
    }
}
</script>

<style scoped>
.input_file {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
}

.custom-file-input:lang(en) ~ .custom-file-label::after {
    content: 'Procurar';
}

</style>
<template>
    <div>
        <b-card 
            no-body 
        >
            <b-row no-gutters>
            <b-col cols="12" md="6">
                <b-card-img 
                    :src="getSelectedImage() || defaultImage"
                    img-alt="Image" 
                    class="rounded-0" 
                    width="400"
                    height="400"
                />
            </b-col>
            <b-col cols="12" md="6">
                <b-card-body title="Face Predictor">
                    <b-card-text>
                        <b-form-file
                            v-model="file"
                            :state="Boolean(file)"
                            placeholder="Escoha uma imagem..."
                            drop-placeholder="Solte aqui"
                            accept=".jpg, .png"
                            browse-text="Procurar"
                            :file-name-formatter="formatFileName"
                        />
                    </b-card-text>
                    <div class="d-flex justify-content-center mt-2 mb-0">
                        <button 
                            type="button" 
                            :title="!file ? 'Selecione uma imagem' : ''"
                            class="btn btn-primary"
                            @click="findFaces()"
                            :disabled="!file"
                        >
                            Enviar
                        </button>
                    </div>
                </b-card-body>
            </b-col>
            </b-row>
        </b-card>
    </div>
</template>

<script>
import defaultImage from '@/static/images/default-image.png';

export default {
    data () {
        return {
            file: null,
            selectedImage: null,
            defaultImage
        }
    },
    methods: {
        formatFileName(file) {
            if (file.length) {
                return 'imagem-alvo'
            }
            return 'Escolha um arquivo'
        },

        async findFaces () {
            try {
                this.$store.dispatch('loader/switchLoader')
                const faces = await this.$store.dispatch('facePredictor/findFaces', this.file)
                this.callFacePredictViewer(faces)
                this.showAlert('success', {
                    title: 'Sucesso', 
                    body: `Rostos encotrados: ${faces.result.faces_count}`}
                )
            } catch (error) {
                console.log(error)
                this.showAlert('danger', 
                    {
                        body: error.message,
                        title: 'Erro'
                    }
                )
            } finally {
                this.$store.dispatch('loader/switchLoader')
                return
            }
        },

        showAlert (variant, {title, body}) {
            this.$bvToast.toast(body, {
                title,
                autoHideDelay: 7000,
                variant
            })
        },

        callFacePredictViewer (faces) {
            this.clearImagesFromFacePredictViewer()
            const imagesBase64 = faces?.result?.faces_images
            this.$bus.$emit('show-image', imagesBase64)
        },

        clearImagesFromFacePredictViewer () {
            this.$bus.$emit('clear-images')
        },

        getSelectedImage () {
            this.clearImagesFromFacePredictViewer()
            if (!this.file) {
                return
            }
            let base64 = ''
            const reader = new FileReader()
            reader.onloadend = () => {
                base64 = reader.result
                this.selectedImage = base64
            }
            reader.readAsDataURL(this.file)
            return this.selectedImage
        }
    }
}
</script>

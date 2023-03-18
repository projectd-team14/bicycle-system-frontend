<template>
    <v-card
        class="mx-auto box"
        max-height="705"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">範囲設定<v-icon>mdi-minus</v-icon>{{ this.cameraName }}</v-card-title>
            <v-col cols="12">
                <img id="img_source" :src="imageSrc" v-on:load="setImage()" cover>
                <canvas
                    id="canvas"
                    :style="('width: 100%; height: 100%;')"
                ></canvas>            
            </v-col>
        </v-card-item>
    </v-card>
</template>
  
<script>
export default {
    data() {
        return {
            cameraName: "",
            imageSrc: "",
            image: null,
            cvs: null,
            ctx: null,
        }
    },
    mounted() {
        this.imageSrc = this.$config.fastURL + "/label/?id=" + this.$route.params.cameras_id;
        console.log(this.imageSrc);
    },
    methods: {
        setImage() {
            this.cvs = document.getElementById('canvas');
            this.ctx = this.cvs.getContext('2d'); 
            this.image = document.getElementById("img_source"); 
            this.cvs.width  = this.image.width;
            this.cvs.height = this.image.height;
            this.ctx.drawImage(this.image, 0, 0); 
            const element = document.getElementById("img_source"); 
            element.remove();
        }
    }
}
</script>

<style scoped>
.box {
    overflow-y: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.box::-webkit-scrollbar {
    display:none;
}
</style>
<template>
    <v-row>
        <v-col cols="12">
            <v-card
                class="mx-auto box"
                height="770"
                style="background: #2c2d3f;"
            > 
                <v-card-item>
                    <v-card-title class="headline">範囲設定<v-icon>mdi-minus</v-icon>{{ this.cameraName }}</v-card-title>
                    <v-col cols="12">
                        <img id="img_source" :src="imageSrc" v-on:load="setImage()" cover>
                        <canvas id="canvas" :style="('width: 100%; height: 100%;')" @click="drawSquare"></canvas>
                    </v-col>
                </v-card-item>
            </v-card>
        </v-col>
        <v-col cols="12">
            <v-card
                class="mx-auto"
                max-height="600"
                style="background: #2c2d3f;"
            > 
                <v-card-item>
                    <v-col cols="12">
                        <v-row>
                            <v-col cols="6">
                                <v-btn
                                    block
                                    style="background: linear-gradient(#e00083, #33005e);"
                                    @click="onClickSaveButton()"
                                >
                                    Save area
                                </v-btn>
                            </v-col>
                            <v-col cols="6">
                                <v-btn
                                    block
                                    outlined
                                    color="#e00083" 
                                    @click="onClickPostButton()"
                                >
                                    Register
                                </v-btn>                          
                            </v-col>                        
                        </v-row>                        
                    </v-col>
                </v-card-item>
            </v-card>   
        </v-col>
    </v-row>
</template>
  
<script>
export default {
    data() {
        return {
            points: [],
            postPoins: [],
            data: [],
            coord: [],            
            coordarr: {},            
            rateWidth: null,
            rateHeight: null,
            image: null,
            cvs: null,
            ctx: null,            
            checkbox: false,
            cameraName: "None",
            imageSrc: ""
        }
    },
    mounted() {
        var camerasData = this.$store.state.cameraData.cameraData;

        for (let i = 0; i < camerasData.length; i++) {
            if (camerasData[i].cameras_id == this.$route.params.cameras_id) {
                this.cameraName = camerasData[i].cameras_name;

                break;
            }
        }

        this.points = [];
        this.postPoins = [];
        this.data = [];
        this.coord = [];
        this.coordarr = {};
        this.rateWidth = null;
        this.rateHeight = null;
        this.image = null;
        this.cvs = null;
        this.ctx = null;

        this.imageSrc = this.$config.fastURL + "/label/?id=" + this.$route.params.cameras_id;
    },
    methods: {
        async setImage() {
            this.cvs = document.getElementById('canvas');
            this.ctx = this.cvs.getContext('2d'); 
            this.image = document.getElementById("img_source"); 
            this.cvs.width  = this.image.width;
            this.cvs.height = this.image.height;
            this.ctx.drawImage(this.image, 0, 0); 
            const element = document.getElementById("img_source"); 
            element.remove();
        },
        async drawSquare(e) {
            // 縦横比の変換処理を入れる
            var clientWidth  = document.getElementById('canvas').clientWidth;
            var clientHeight = document.getElementById('canvas').clientHeight;
            this.rateWidth = clientWidth  / this.image.width; 
            this.rateHeight = clientHeight / this.image.height; 
            var rect = e.target.getBoundingClientRect();
            var x = (e.clientX - rect.left) / this.rateWidth;
            var y = (e.clientY - rect.top) / this.rateHeight;
            this.points.push([x,y]);
            
            if (this.points.length > 4){
                points.shift();
            }

            this.ctx.clearRect(0, 0, this.cvs.width, this.cvs.height);
            this.ctx.strokeStyle = "#14ff10";
            this.ctx.fillStyle = "#ff6b6b";
            this.ctx.lineWidth = 2;
            
            for (let i in this.points){
                this.ctx.drawImage(this.image,0,0); 
                this.ctx.beginPath();
                this.ctx.arc(this.points[i][0], this.points[i][1], 3, 0, Math.PI*2, true);
                this.ctx.fill();
            }
            
            if (this.points.length === 4) {
                let p = this.points.slice(0, this.points.length);
                let s = [];
                let isCross = function(line1, line2) {
                    var l1From = line1[0];
                    var l1To = line1[1];
                    var l2From = line2[0];
                    var l2To = line2[1];
                    var lineFormula = function(l){
                        return l[1] - l1From[1] - (l[0]-l1From[0]) * (l1To[1] - l1From[1]) / (l1To[0] - l1From[0]);
                    }

                    return lineFormula(l2From)*lineFormula(l2To)<0;
                }

                if (isCross([p[0], p[1]] , [p[2], p[3]])){
                    s = [p[0], p[2], p[1] , p[3]];
                }
                else if (isCross([p[0], p[2]] , [p[1], p[3]])){
                    s = [p[0], p[1], p[2] , p[3]];
                }
                else {
                    s = [p[0], p[1], p[3] , p[2]];
                }
                
                for (let i = 0; i < s.length; i++){
                    this.ctx.beginPath();
                    this.ctx.moveTo(s[i][0], s[i][1]);
                    let k = (i === s.length - 1 ? 0 : i + 1);
                    this.ctx.lineTo(s[k][0], s[k][1]);
                    this.ctx.stroke();
                }

                var r = Math.floor(Math.random() * 200);
                var g = Math.floor(Math.random() * 200);
                var b = Math.floor(Math.random() * 200);
                var color = "rgba(" + r + "," + g + "," + b + ",0.5)";
                this.coord = [s[0], s[1], s[2], s[3], color];
                this.points = [];
            }

            for (var i = 0; i < this.postPoins.length; i++) {
                this.ctx.beginPath();
                this.ctx.fillStyle = this.postPoins[i][4];
                this.ctx.moveTo(this.postPoins[i][0][0], this.postPoins[i][0][1]);
                this.ctx.lineTo(this.postPoins[i][1][0], this.postPoins[i][1][1]);
                this.ctx.lineTo(this.postPoins[i][2][0], this.postPoins[i][2][1]);
                this.ctx.lineTo(this.postPoins[i][3][0], this.postPoins[i][3][1]);
                this.ctx.closePath();
                this.ctx.fill();   
            }
        },
        async onClickSaveButton() {
            if (this.coord.length === 5){
                this.postPoins.push(this.coord);
                this.ctx.beginPath();
                this.ctx.fillStyle = this.coord[4];
                this.ctx.moveTo(this.coord[0][0], this.coord[0][1]);
                this.ctx.lineTo(this.coord[1][0], this.coord[1][1]);
                this.ctx.lineTo(this.coord[2][0], this.coord[2][1]);
                this.ctx.lineTo(this.coord[3][0], this.coord[3][1]);
                this.ctx.closePath();
                this.ctx.fill();
            }
        },
        async onClickPostButton() {
            this.data =[];

            for (var i = 0; i < this.postPoins.length; i++) {
                var jsonTemplate = {
                    "label_mark": i,
                    "label_point1X" : this.postPoins[i][0][0],
                    "label_point1Y" : this.postPoins[i][0][1],
                    "label_point2X" : this.postPoins[i][1][0],
                    "label_point2Y" : this.postPoins[i][1][1],
                    "label_point3X" : this.postPoins[i][2][0],
                    "label_point3Y" : this.postPoins[i][2][1],
                    "label_point4X" : this.postPoins[i][3][0],
                    "label_point4Y" : this.postPoins[i][3][1]
                };
                this.data.push(jsonTemplate);
            }

            this.storeLabel();
        },
        async storeLabel() {
            this.$axios.post("/api/labels/" + this.$route.params.cameras_id, this.data)
            .then((response) => {
                this.onLoadhomeData();
                this.$router.push("/home");
            })
        },
        onLoadhomeData() {
            this.$store.dispatch("homeData/onLoadHomeData", {
                usersId: this.$auth.user.id
            });
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
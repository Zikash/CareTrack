<template>
            <div class="main">
                <div class="headbar">
                    <h2 
                    @click="infoPage = 'patient'" 
                    class="name profile" 
                    :class="{
                        thenPage: infoPage === 'patient'
                    }">Пациент</h2>

                    <h2
                    @click="infoPage = 'osmotrs'" 
                    class="name osmotrs" 
                    :class="{
                        'thenPage': infoPage === 'osmotrs' || infoPage === 'osmotr'
                    }">Осмотры</h2>
                </div>
                
            
                <div class="main__view">

                    <div class="patient_profile" v-if="infoPage === 'patient'">
                        <div class="rootBox">
                            <h2 class="root">Информация о пациенте</h2>
                        </div>
                        
                        <h3>ФИО</h3>
                        <div class="content_profile">
                            <h3>{{ info.patient.Fio }}</h3>
                        </div>
                        <h3>Телефон</h3>
                        <div class="content_profile">
                            <h3>{{info.patient.phone}}</h3>
                        </div>
                        <h3>Адрес</h3>
                        <div class="content_profile">
                            <h3>{{info.patient.home_address}}</h3>
                        </div>
                        <h3>Возраст</h3>
                        <div class="content_profile">
                            <h3>{{info.patient.Age}}</h3>
                        </div>
                        <h3>Пол</h3>
                        <div class="content_profile">
                            <h3>{{info.patient.Gender}}</h3>
                        </div>

                    </div>
                        
                    <div class="patient_osmotrs" v-else-if="infoPage === 'osmotrs'">
                        <osmotr-bar 
                        @SelectOsmotr="SelectOsmotr"
                        v-for="osmotr in info.osmotrs.slice(page*limit-limit, page*limit)" 
                        v-if="info.osmotrs.length >= 1"
                        :osmotr="osmotr"/>
                        <h2 v-else>Осмотров нет</h2>

                        <div class="page_wrapper">
                            <h3 v-for="Npage in totalPages"
                            class="page_number"
                            :key="Npage"
                            :class="{
                                'this_page': page === Npage
                            }"
                            @click="page = Npage">{{ Npage }}</h3>
                        </div>


                    </div>
                    <div class="patient_osmotr" v-else-if="infoPage === 'osmotr'">

                        <div class="boxBack"> 
                            <button @click="backOsmotr" class="back"><</button>
                        </div>
                        <div class="rootBox">
                            <h2 class="root">Информация о осмотре</h2>
                        </div>
                        
                        <h3>Место осмотра</h3>
                        <div class="content_profile">
                            <h3 v-if="info.osmotr.serviced_area_number === 'Hospital'">Больница</h3>
                            <h3 v-else>{{ info.osmotr.patient.home_address }}</h3>
                        </div>
                        <h3>Дата осмотра</h3>
                        <div class="content_profile">
                            <h3>{{info.osmotr.Date_this}}</h3>
                        </div>
                        <h3>Врач</h3>
                        <div class="content_profile">
                            <h3>{{info.osmotr.doctor.Fio}}</h3>
                        </div>
                        <h3>Пациент</h3>
                        <div class="content_profile">
                            <h3>{{info.osmotr.patient.Fio}}</h3>
                        </div>
                        <h3>Симптомы</h3>
                        <div class="content_profile">
                            <h3 v-for="simptome in info.osmotr.Simptomes"
                            class="simptom">{{simptome}}</h3>
                        </div>
                        <h3>Диагноз</h3>
                        <div class="content_profile">
                            <h3>{{info.osmotr.Result}}</h3>
                        </div>
                        <h3>Предписания</h3>
                        <div class="content_profile">
                            <h3>{{info.osmotr.Predpis}}</h3>
                        </div>

                    </div>

                        

                </div>
                    
            </div>

</template>

<script>

    export default {
        name: 'patient-info',
        props: {
            info: {
                Type: Object,
                required: true
            }
        },
        data() {
            return {
                infoPage: 'patient',
                limit: 10,
                page: 1,
                totalPages: 0
            }
        },
        watch: {
            infoPage() {
                this.page = 1
                this.totalPages = Math.ceil(this.info.osmotrs.length / this.limit)
            }
        },
        methods: {
            SelectOsmotr(osmotr){

                this.infoPage = 'osmotr'
                this.info.osmotr = osmotr

            },
            backOsmotr() {
                this.infoPage = 'osmotrs'
                this.info.osmotr = {}
            }
        }
    }
</script>

<style scoped>

input {
background-color: #F0EEEE;
}

textarea {
background-color: #F0EEEE;
}


form {
display: flex;
margin-left: auto;
margin-right: auto;
}

.main_div {
display:flex;
flex-wrap: wrap;
margin-top: 20px;
margin-left: auto;
margin-right: auto;
min-width: 500px;
}

.main {
margin-top: 20px;
margin-left: auto;
margin-right: auto;
min-width: 500px;
}

.headbar {
display: flex;

}


.name {
background-color: white;
border-radius: 10px 10px 0 0;
align-content: center;
text-align: center;
width: 100%;
padding: 15px;
height: 50px;
}

.profile {
    box-shadow: -3px -3px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.doctors {
    box-shadow: 0px -2px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.patients {
    box-shadow: 0px -2px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.osmotrs {
    box-shadow: 3px -3px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.thenPage {
    box-shadow: 0px 0px 0px 0px rgba(34, 60, 80, 0.2) inset;
}



.main__view {
background-color: white;
padding: 35px;
margin-left: auto;
margin-right: auto;
border-radius: 0px 10px 10px 10px;
}

.rootBox {
    padding-left: 40px;
    padding-right: 40px;
    margin-bottom: 40px;
}

.root {
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    align-content: center;
    background-color: #D9D9D9;
    height: 40px;
    border-radius: 5px;
}

.content_profile {
    display: flex;
    margin-top: 8px;
    margin-bottom: 15px;
}

.content_profile h3 {
    background-color: #D9D9D9;
    padding: 5px;
    border-radius: 5px;
}

.content_profile button {
    background-color: #69C553;
    border-radius: 5px;
    padding: 5px;
    margin-left: 20px;
}

.exitBox {
    display: flex;
}

.exit {
    background-color: #B83E40;
    border-radius: 5px;
    padding: 8px;
    margin-top: 10px;
    margin-left: auto;
    margin-right: 20px;
}


.boxBack {
    display: flex;
    margin-bottom: 30px;
}

.back {
    height: 40px;
    width: 60px;
    margin-left: auto;
    margin-right: auto;
}

.simptom {
    margin-left: 5px;
}

.page_wrapper {
    margin-left:auto;
    display: flex;
    padding: 5px;
}

.page_number {
    margin-left: 10px;
    border: 2px black;
    padding: 10px;
    box-sizing: border-box;
    background-color: #69C553;
}

.this_page {
    background-color: green;
}

</style>
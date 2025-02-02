import { createStore } from "vuex"; 

export default createStore({
    state: () => ({
        patient: {
            Fio: "Haruton ebrog Afomon",
            Phone: "8 888 099 73-89",
            Gender: "М",
            Mail: 'nePisat@otveta.net',
            Age: 6
        },
        doctor: null,
        administrator: {
            Phone: '8 800 535-35-35',
            Mail: 'nePisat@otveta.net'
        },
        auth: "auth"
    }),
    getters: {
        isAuth(state) {
            if (state.patient != null || state.doctor != null || state.administrator != null){
                return true
            }
            return false
        }
    },
    mutations: {
        updatePatient(state, patient) {
            state.patient = patient
        },
        updateDoctor(state, doctor){
            state.doctor = doctor
        },
        updateAdministrator(state, administrator){
            state.administrator = administrator
        },
        updateAuth(state, auth){
            state.auth = auth
        }
    }
})
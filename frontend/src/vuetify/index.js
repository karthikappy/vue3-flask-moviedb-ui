import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

const vuetify = createVuetify({
        components,
        directives,
        icons: {
                defaultSet: 'mdi',
                aliases,
                sets: {
                    mdi,
                },
        },
        ssr: true,
        theme: {
            defaultTheme: 'dark'
        }
})
export default vuetify
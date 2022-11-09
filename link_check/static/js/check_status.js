$(document).ready(function () {
    $('.checkAllStatusesBtn').on('click', function () {
        let row, rowStatus

        $.get('/api/links').done(function (data) {
            for (const item of data) {
                const { id, status } = item

                row = $(`tr[data-id="${id}"]`)
                rowStatus = status === 200 ? 'green' : 'red'

                $(row).attr('data-status', rowStatus)
                $('.status', row).text(status)
            }
        })
    })

    $('.checkStatusBtn').on('click', function () {
        const id = $(this).attr('data-id')
        const row = $(`tr[data-id="${id}"]`)

        $.get('/api/links/' + id).done(function (data) {
            const {status} = data
            const rowStatus = status === 200 ? 'green' : 'red'

            $(row).attr('data-status', rowStatus)
            $('.status', row).text(status)
        })
    })
})
$(document).ready(function () {
    const apiPath = '/api/status'

    $('tr.row').each(function () {
        const row = this
        const url = $(this).attr('data-testid')
        const interval = parseInt($(this).attr('data-interval'))

        setInterval(() => {
            $(row).attr('data-status', '')
            $('.comment', row).removeClass('hidden')

            $.post(apiPath, {url: url}).done(function (data) {
                $('.comment', row).addClass('hidden')

                const {status} = data
                const rowStatus = status === 200 ? 'green' : 'red'

                $(row).attr('data-status', rowStatus)
                $('.status', row).text(status)
            })
        }, interval * 1000)
    })
})
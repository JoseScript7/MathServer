from django.shortcuts import render

def power(request):
    context = {
        'i': "0",   # Default intensity value
        'r': "0",   # Default resistance value
        'power': "0"  # Default power value
    }

    if request.method == 'POST':
        intensity = request.POST.get('intensity', '0')
        resistance = request.POST.get('resistance', '0')

        try:
            # Convert values to integers for calculation
            i = int(intensity)
            r = int(resistance)

            # Calculate power using P = I^2 * R
            power = i * i * r
        except ValueError:
            # Handle invalid input values gracefully
            power = "Invalid input"

        # Update the context with calculated or error values
        context['i'] = intensity
        context['r'] = resistance
        context['power'] = power

    return render(request, 'mathapp/math.html', context)


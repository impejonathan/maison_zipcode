from django import forms

class HousePredictionForm(forms.Form):
    BEDROOM_CHOICES = [(i, str(i)) for i in range(0, 16)]
    bedrooms = forms.ChoiceField(label="Nombre de chambres", choices=BEDROOM_CHOICES, 
                                 error_messages={'required': "Veuillez indiquer le nombre de chambres"})
    
    BATHROOM_CHOICES = [(i, str(i)) for i in range(0, 16)]
    bathrooms = forms.ChoiceField(label="Nombre de salles de bain", choices=BATHROOM_CHOICES, 
                                  error_messages={'required': "Veuillez indiquer le nombre de salles de bain"})
    
    sqft_living = forms.IntegerField(label="Surface à vivre (en pieds carrés)" ,initial=0)
    
    sqft_lot = forms.IntegerField(label="Surface du terrain (en pieds carrés)" ,initial=0)
    
    FLOOR_CHOICES = (
        (0.0, '0.0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4')
    )

    floors = forms.ChoiceField(label="Nombre d'étages", choices=FLOOR_CHOICES, error_messages={'required': "Veuillez indiquer le nombre d'étages"})

    
    waterfront = forms.BooleanField(label="Vue sur le lac", required=False)
        
    VIEW_CHOICES = [(i, str(i)) for i in range(5)]
    view = forms.ChoiceField(label="Qualité de la vue (de 0 à 4)", choices=VIEW_CHOICES, initial=0, 
                            error_messages={'required': "Veuillez indiquer la qualité de la vue"})

    GRADE_CHOICES = [(i, str(i)) for i in range(14)]
    grade = forms.ChoiceField(label="Qualité de la construction (de 0 à 13)", choices=GRADE_CHOICES, initial=0, 
                            error_messages={'required': "Veuillez indiquer la qualité de la construction"})

    
    sqft_basement = forms.IntegerField(label="Surface du sous-sol (en pieds carrés)", min_value=0, required=False, initial=0,)
    
    yr_renovated = forms.IntegerField(label="Années depuis la rénovation ou la construction", required=False, initial=0,)
    
    # zipcode = forms.CharField(max_length=5, label="Code postal",
    #                           error_messages={'required': "Veuillez indiquer le code postal",
    #                                           'max_length': "Le code postal doit comporter exactement 5 caractères"})
    ZIPCODE_CHOICES = (
    (98002, '98002'), (98166, '98166'), (98168, '98168'), (98144, '98144'), (98178, '98178'), (98108, '98108'),
    (98032, '98032'), (98055, '98055'), (98118, '98118'), (98122, '98122'), (98115, '98115'), (98007, '98007'),
    (98034, '98034'), (98052, '98052'), (98042, '98042'), (98040, '98040'), (98136, '98136'), (98126, '98126'),
    (98146, '98146'), (98188, '98188'), (98059, '98059'), (98109, '98109'), (98116, '98116'), (98103, '98103'),
    (98006, '98006'), (98075, '98075'), (98024, '98024'), (98155, '98155'), (98003, '98003'), (98023, '98023'),
    (98117, '98117'), (98177, '98177'), (98019, '98019'), (98028, '98028'), (98092, '98092'), (98022, '98022'),
    (98070, '98070'), (98038, '98038'), (98107, '98107'), (98106, '98106'), (98065, '98065'), (98053, '98053'),
    (98072, '98072'), (98077, '98077'), (98133, '98133'), (98001, '98001'), (98056, '98056'), (98045, '98045'),
    (98033, '98033'), (98011, '98011'), (98014, '98014'), (98199, '98199'), (98008, '98008'), (98031, '98031'),
    (98004, '98004'), (98074, '98074'), (98030, '98030'), (98027, '98027'), (98029, '98029'), (98058, '98058'),
    (98010, '98010'), (98005, '98005'), (98198, '98198'), (98148, '98148'), (98112, '98112'), (98125, '98125'),
    (98105, '98105'), (98102, '98102'), (98119, '98119'), (98039, '98039'),
)

    
    zipcode = forms.TypedChoiceField(coerce=int ,label="liste des code postal", choices=ZIPCODE_CHOICES, error_messages={'required': " pas de code postal"})
    
    # lat = forms.DecimalField(label="Latitude", max_digits=10, decimal_places=6, initial=0,)
    # long = forms.DecimalField(label="Longitude", max_digits=10, decimal_places=6, initial=0,)

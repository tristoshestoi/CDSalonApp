from django import forms
from .models import CD, CdHasAlbum, Album, SellArrival, Track
from django.views.generic.edit import CreateView
from .models import company_maker

class CDForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = [
            "name",
            "price",
            "create_date",
            "company_id",
        ]


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = [
            "track_name",
            "author",
            "performer",
            "album_id",
        ]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "album_name",
            "track_amount",
            "genre",
            "length",
            "out_date",
        ]


class ArrivalForm(forms.ModelForm):
    class Meta:
        model = SellArrival
        fields = [
            "CD_id",
            "op_date",
            "supplier",
            "amount",
            "price",
            "op_code",

        ]


class AlbumCDForm(forms.ModelForm):
    class Meta:
        model = CdHasAlbum
        fields = [
            "CD_id",
            "Album_id",
        ]
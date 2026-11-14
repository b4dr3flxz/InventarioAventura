from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cuentas.models import Perfil


class RegistroTuristaForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre...'})
    )
    last_name = forms.CharField(
        max_length=50,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Apellido...'})
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Correo electrónico...'})
    )
    telefono = forms.CharField(
        max_length=20,
        required=False,
        label='Teléfono',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Teléfono (opcional)...'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Nombre de usuario...'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Contraseña...'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Repetir contraseña...'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Perfil.objects.create(
                user=user,
                rol='Turista',
                telefono=self.cleaned_data.get('telefono', '')
            )
        return user


class UsuarioAdminForm(forms.ModelForm):
    password = forms.CharField(required=False, label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    rol = forms.ChoiceField(choices=Perfil.ROLES, label='Rol', widget=forms.Select(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=20, required=False, label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control'}))
    especialidad = forms.CharField(max_length=120, required=False, label='Especialidad', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            perfil, _ = Perfil.objects.get_or_create(user=self.instance)
            self.fields['rol'].initial = perfil.rol_normalizado()
            self.fields['telefono'].initial = perfil.telefono
            self.fields['especialidad'].initial = perfil.especialidad

    def save(self, commit=True):
        user = super().save(commit=False)
        clave = self.cleaned_data.get('password')
        if clave:
            user.set_password(clave)
        elif not user.pk:
            user.set_password('Aventura2026!')
        if not user.is_superuser:
            user.is_staff = (self.cleaned_data.get('rol') == 'Administrador')
        if commit:
            user.save()
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.rol = self.cleaned_data['rol']
            perfil.telefono = self.cleaned_data.get('telefono', '')
            perfil.especialidad = self.cleaned_data.get('especialidad', '')
            perfil.save()
        return user


class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Perfil
        fields = ['telefono', 'especialidad']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        perfil = super().save(commit=False)
        user = perfil.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            perfil.save()
        return perfil
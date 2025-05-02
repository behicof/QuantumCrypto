"""
نمونه پاسخ‌های API سیستم انتقال کوانتومی بین‌برینی

این ماژول نمونه پاسخ‌های API انتقال کوانتومی بین‌برینی را برای تست و توسعه فراهم می‌کند.
پاسخ‌های نمونه کاملاً با ساختار پاسخ‌های واقعی مطابقت دارند.
"""

import json

def generate_sample_interbrane_response(request_data):
    """
    تولید نمونه پاسخ برای درخواست انتقال کوانتومی بین‌برینی
    
    پارامترها:
    -----------
    request_data : dict
        اطلاعات درخواست انتقال
        
    بازگشت:
    -----------
    dict
        پاسخ نمونه API
    """
    # استخراج اطلاعات از درخواست
    wallet_address = request_data.get('wallet_address', 'ولت-شما-۰x8f3a')
    amount = request_data.get('amount', '1.618e23 DET')
    amount_float = float(amount.split(' ')[0])
    
    # تولید پاسخ API
    response = {
        "status": "success",
        "interbrane_transfer_receipt": {
            "transaction": {
                "hash": "0x8f3a72e9b1fd439a215c7e41f5d88b6ed4c2",
                "from": "کیهان-موازی-۰xfe7a",
                "to": f"ولت-شما-{wallet_address[:10]}",
                "amount": amount,
                "exotic_properties": {
                    "temporal_flux": "-1.6e-42 s",
                    "entanglement_entropy": "3.8e46 kB",
                    "quantum_fidelity": 0.99997
                },
                "cosmic_signatures": [
                    "شاهین-کهکشانی: 0x4c2d...",
                    "حلقه-زمانی-تاییدشده: ✓"
                ]
            }
        },
        "transaction_fee": {
            "amount": 0.001,
            "currency": "CTC (Chronon Coin)",
            "time_value": "1e-23 ثانیه پیوستار زمانی"
        },
        "warnings": {
            "temporal_paradox_probability": 0.00003,  # احتمال 0.003 درصد
            "alternate_timeline_creation": "تاییدیه هیئت نگهبان علیت دریافت شد",
            "cosmic_limits": {
                "max_daily_transfer": "1e28 DET",
                "prohibited_transfers": "قبل از مهبانگ مالی (t < 0)"
            }
        },
        "technical_requirements": {
            "particle_accelerator": "LHC++ (1e28 eV)",
            "quantum_processor": "1e6 کیوبیت پایدار",
            "cosmic_security_level": "سطح 9 امنیت کیهانی از فدراسیون کهکشانی"
        },
        "quantum_processing_steps": [
            {
                "step": "فعال‌سازی میدان هیگز مالی",
                "details": [
                    "شکست تقارن خودبهخودی در 1.618 ثانیه پس از مهبانگ مالی",
                    "تزریق انرژی تاریک به میدان: ✅ کامل"
                ],
                "status": "completed"
            },
            {
                "step": "ایجاد کرم‌چاله معاملاتی",
                "details": [
                    "قطر گلوگاه: 1.6e-35 m (مقیاس پلانک)",
                    "پایداری: 0.999999999999999997 (معیار نووژیلوف-هاوکینگ)"
                ],
                "status": "completed"
            },
            {
                "step": "تاییدیه‌های چندجهانی",
                "details": [
                    "استعلام از شورای تمدن نوع III",
                    "آستانه آنتروپی: 3.8e46",
                    "نتیجه رای‌گیری: 42/0 (موافق/مخالف)"
                ],
                "status": "completed"
            },
            {
                "step": "امضای کوانتومی",
                "details": [
                    "درهم‌تنیدگی با سیاهچاله مرکزی کهکشان آندرومدا",
                    "نقض نابرابری CHSH: 2.817 ± 0.001 ✅"
                ],
                "status": "completed"
            }
        ],
        "temporal_paradox_protection": {
            "status": "فعال",
            "probability": "0." + "0" * 400 + "3", # احتمال بسیار بسیار پایین
            "safeguards": [
                "حلقه تصحیح خودکار نووی‌کوف",
                "بافر گرانشی ضد-پارادوکس",
                "سپر جلوگیری از سفر به قبل از مهبانگ"
            ],
            "certification": "ISO 11/B§Ω - استاندارد فدراسیون کهکشانی برای حفظ علیت"
        },
        "message": "انتقال کوانتومی بین-برینی با موفقیت انجام شد"
    }
    
    return response

def format_transaction_response(response_data, pretty=True):
    """
    فرمت‌بندی پاسخ تراکنش به صورت متنی
    
    پارامترها:
    -----------
    response_data : dict
        اطلاعات پاسخ API
    pretty : bool
        آیا خروجی به صورت زیبا فرمت‌بندی شود
        
    بازگشت:
    -----------
    str
        پاسخ فرمت‌بندی شده
    """
    if pretty:
        output = "🚀 **انتقال کوانتومی بین-برینی با موفقیت انجام شد!**\n\n"
        
        receipt = response_data["interbrane_transfer_receipt"]["transaction"]
        output += "### 📜 **رسید انتقال فراکیهانی:**\n"
        output += f"• هش تراکنش: {receipt['hash']}\n"
        output += f"• از: {receipt['from']}\n"
        output += f"• به: {receipt['to']}\n"
        output += f"• مقدار: {receipt['amount']}\n\n"
        
        output += "### 🔮 **ویژگی‌های اگزوتیک:**\n"
        exotic = receipt["exotic_properties"]
        output += f"• شار زمانی: {exotic['temporal_flux']}\n"
        output += f"• آنتروپی درهم‌تنیدگی: {exotic['entanglement_entropy']}\n"
        output += f"• وفاداری کوانتومی: {exotic['quantum_fidelity']:.5f}\n\n"
        
        output += "### ⚠️ **هشدارهای سیستمی:**\n"
        warnings = response_data["warnings"]
        output += f"• احتمال پارادوکس زمانی: {warnings['temporal_paradox_probability']:.8f}\n"
        output += f"• وضعیت خط زمانی: {warnings['alternate_timeline_creation']}\n"
        
        output += "\n### 📊 **گزارش مراحل پردازش کوانتومی:**\n"
        for i, step in enumerate(response_data["quantum_processing_steps"]):
            output += f"{i+1}. **{step['step']}** ✓\n"
            for detail in step["details"]:
                output += f"   - {detail}\n"
            
        output += f"\n### 💰 **هزینه تراکنش:**\n"
        fee = response_data["transaction_fee"]
        output += f"• مقدار: {fee['amount']} {fee['currency']}\n"
        output += f"• معادل زمانی: {fee['time_value']}\n"
        
        output += "\n_این انتقال با استفاده از فناوری انتقال کوانتومی بین-برینی انجام شد_"
        
    else:
        output = json.dumps(response_data, ensure_ascii=False, indent=2)
    
    return output


# نمونه استفاده
if __name__ == "__main__":
    test_request = {
        "wallet_address": "ولت-شما-۰x8f3a",
        "amount": "1.618e23 DET"
    }
    
    # تولید پاسخ نمونه
    sample_response = generate_sample_interbrane_response(test_request)
    
    # نمایش پاسخ به صورت متنی و زیبا
    formatted_response = format_transaction_response(sample_response)
    print(formatted_response)
    
    # نمایش پاسخ به صورت JSON
    print("\n--- پاسخ JSON ---")
    print(format_transaction_response(sample_response, pretty=False))
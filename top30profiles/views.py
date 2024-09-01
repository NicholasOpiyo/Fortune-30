
from pyclbr import Class
from django.shortcuts import render


from top30profiles.models import InitialInsights

# Query set
initial_profile_data = InitialInsights.objects.all()

# Building dictionaries from query set and collecting list of industries
  # List of dictionaries created from query set
company_profiles = []
  # List of the values of the 'industry' field
sectors = []

for i in initial_profile_data:
    company_name = i.company
    company_revenue = i.revenue
    # Transforming values from 'revenue' and 'employee' field into easily readable format
    revenue_in_billions = "{:.2f}".format(company_revenue/1000)
    revenue_string = f"${revenue_in_billions} billion"
    company_employees = f"{i.employees: ,}"
    # Changing the value of the record whose 'industry' field has 'Discount Stores' value
    company_industry = i.industry
    if company_industry == 'Discount Stores':
        company_industry = 'Discount stores'
    company_headquarters = i.headquarters
    company_rank = i.fortune_100_rank
    # Changing the value of each record's 'logo' field
    company_logo = 'images/' + i.logo
    # Creating a dictionary from each record
    profiled_company = {'company':company_name, 'revenue':revenue_string, 
                        'employees':company_employees,'industry':company_industry, 
                        'headquarters':company_headquarters, 
                        'rank':company_rank, 'logo':company_logo}
    # Adding each dictionary to the 'company_profiles' list
    company_profiles.append(profiled_company)
    # Adding each record's 'industry' field to 'sectors' list
    sectors.append(company_industry)

# Changing value of 'logo' field of two companies that lack suitable logos
company_profiles[3]['logo'] = 'images/iac.svg'
company_profiles[26]['logo'] = 'images/iac.svg'

# Building dictionary from collected dictionaries
profiled_companies = {}
for c in range(len(company_profiles)):
    profiled_companies[c] = company_profiles[c]

# Removing repetitive elements from 'sectors' list
for s in sectors:
    if sectors.count(s) > 1:
        while sectors.count(s) > 1:
            sectors.pop(sectors.index(s))

# Sorting 'sectors' list alphabetically
sectors.sort()

# Breakdown of companies by industry
  # Creating list of industry lists
companies_by_sector = []
for s in sectors:
    companies_by_sector.append([])
  # Adding dictionaries to the lists in 'companies_by_sector' list
for s in sectors:
    # Matching dictionaries' 'industry' field to elements of 'sectors' list
    for p in company_profiles:
        if p['industry'] == s:
            # Collecting dictionaries with the same value for 'industry' field
            list_to_fill = companies_by_sector[sectors.index(s)]
            list_to_fill.append(p)
  # Mapping industries to dictionaries that share the same value for 'industry' field
sector_breakdown = {}
for s in sectors:
    sector_breakdown[s] = companies_by_sector[sectors.index(s)]

# Method for obtaining 'sectors' list
def get_sectors():
    return sectors

# View for 'index' endpoint
def initial_insights(request):
    return render(request,'index.html', {'profiles': profiled_companies, 
                  'plength':len(initial_profile_data)})

# View for 'industries' endpoint
def industries(request):
    return render(request,'industries.html', {'profiles': profiled_companies, 
                 'sectors':sectors, 'plength':len(initial_profile_data)
                  })

# View for 'specific industry' endpoint
def specific_industry(request):    
    sector = request.POST.get('industry') 
    companies = sector_breakdown[sector]
    sector_length = len(companies)
    return render(request,'industry.html', {'companies': companies,
                 'plength':len(initial_profile_data), 'sector': sector,
                 'slength':sector_length, 'sectors':sectors})


    
     



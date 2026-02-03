library(tidyverse)
library(ggplot2)

# Load dataset.
df <- read_csv('toronto-shelter-system-flow.csv')

# Change date name for ease.
colnames(df)[colnames(df)=='date(mmm-yy)'] <- 'date'

# Extract only all population to avoid duplication.
df = df[df[,'population_group']=='All Population',]

# Extract the year only and group by it, then calculate mean and standard error
# across months for that year.
df_stats <- df %>%
  mutate(year=paste0('20',str_sub(date,-2))) %>%
  group_by(year) %>%
  summarize(
    avg_identified=mean(newly_identified),
    sd_identified=sd(newly_identified),
    n = n()
  ) %>%
  mutate(se_identified=sd_identified/sqrt(n))

# Plot newly identified homeless over time.
p <- ggplot(df_stats,aes(x=year,y=avg_identified)) + # Plot mean.
  geom_col(fill='grey') +
  geom_errorbar(aes(ymin=avg_identified-se_identified, 
                    ymax=avg_identified+se_identified), 
                width=0.2,color='black') + # Plot error bars.
  labs(title='Newly Identified Homeless Individuals in Toronto Over Time', # Label, including source of information.
       x='Year',
       y='Number',
       caption='Source: Toronto Shelter & Support Services – Toronto Shelter System Flow (Toronto Open Data)') +
  theme_minimal() + # Set theme with guide lines.
  theme(plot.title = element_text(face='bold'),
        plot.caption = element_text(face='bold',margin=margin(t=15)))
ggsave('vis2_assignment_3.png',p,width=8,height=6) # Save.

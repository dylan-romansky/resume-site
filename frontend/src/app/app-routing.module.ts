import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { ResumeComponent } from './resume/resume.component';
import { AboutMeComponent } from './about-me/about-me.component';
import { EntryComponent } from './entry/entry.component';

const routes: Routes = [
	{path: '', component: HomeComponent},
	{path: 'resume', component: ResumeComponent},
	{path: 'add', component: EntryComponent},
	{path: 'about', component: AboutMeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
